# -*- coding: utf-8 -*-

import os
from fabric.api import cd, run, sudo, prefix, task, env
from fabric.contrib.files import upload_template

env.forward_agent = True

USER = 'vagrant'
PROJECT_DIR = '/home/{USER}/project/eshop/'.format(USER=USER)
DJANGO_DIR = PROJECT_DIR + 'bookshop'
GIT_REPOSITORY = 'https://github.com/daikeren/eshop'
DB_USER = 'django'
DB_PASSWORD = 'django'
DB_NAME = 'eshop'
DATABASE_URL = 'postgres://{0}:{1}@localhost/{2}'.format(DB_USER, DB_PASSWORD, DB_NAME)


def upgrade_system():
    sudo('apt-get update -y')


def install_packages():
    required_packages = [
        'git', 'build-essential',
        'python3-dev', 'python3-minimal', 'python3-venv', 'python3-pip',
        'nginx',
        'libxml2-dev', 'libxslt1-dev',
        'libjpeg-dev', 'libfreetype6', 'libfreetype6-dev', 'zlib1g-dev',
        'postgresql', 'postgresql-server-dev-all', 'libpq-dev',
    ]

    sudo('apt-get install -y {}'.format(' '.join(required_packages)))


def setup_repository():
    run('rm -rf {}'.format(PROJECT_DIR))
    run('git clone {} {}'.format(GIT_REPOSITORY, PROJECT_DIR))


def create_virtualenv():
    with cd(PROJECT_DIR):
        run('python3 -m venv venv')


def install_requirements():
    with prefix('source {}/venv/bin/activate'.format(PROJECT_DIR)):
        run('pip install -r {}'.format(
            os.path.join(PROJECT_DIR, 'requirements.txt')
        ))


def restart_nginx():
    sudo('systemctl restart nginx')


def setup_nginx():
    upload_template(
        filename='config/nginx.conf',
        destination='/etc/nginx/sites-enabled/test.conf',
        context={
            'server_name': 'localhost',
            'static_dir': os.path.join(DJANGO_DIR, 'static'),
            'media_dir': os.path.join(DJANGO_DIR, 'media'),
        },
        use_sudo=True,
        use_jinja=True
    )


def pull_repository():
    with cd(PROJECT_DIR):
        run('git pull origin master')


def _run_as_pg(command):
    return sudo('sudo -u postgres {}'.format(command))

def pg_user_exists(username):
    res = _run_as_pg('''psql -t -A -c "SELECT COUNT(*) FROM pg_user WHERE usename = '{username}';"'''.format(username=username))
    return (res == '1')

def pg_database_exists(database):
    res = _run_as_pg('''psql -t -A -c "SELECT COUNT(*) FROM pg_database WHERE datname = '{database}';"'''.format(database=database))
    return (res == "1")

def pg_create_user(username, password):
    _run_as_pg(
        '''psql -t -A -c "CREATE USER {username} WITH PASSWORD '{password}';"'''.format(
            username=username, password=password)
    )

def pg_create_database(database, owner):
    _run_as_pg('createdb {database} -O {owner}'.format(database=database, owner=owner))

def create_database():
    if not pg_user_exists('django'):
        pg_create_user('django', 'django')
    if not pg_database_exists('eshop'):
        pg_create_database('eshop', 'django')


def create_gunicorn_script():
    upload_template(
        filename='config/run.sh',
        destination=os.path.join(PROJECT_DIR, 'run.sh'),
        context={
            'django_dir': DJANGO_DIR,
            'project_dir': PROJECT_DIR,
            'db_user': DB_USER,
            'db_password': DB_PASSWORD,
            'db_name': DB_NAME,
        },
        use_sudo=True,
        use_jinja=True
    )
    run('chmod 755 {0}'.format(os.path.join(PROJECT_DIR, 'run.sh')))


def restart_service():
    sudo('systemctl restart nginx')
    sudo('systemctl restart gunicorn')


def setup_systemd():
    upload_template(
        filename='config/gunicorn.service',
        destination='/etc/systemd/system/gunicorn.service',
        context={
            'gunicorn_script': os.path.join(PROJECT_DIR, 'run.sh'),
            'project_dir': PROJECT_DIR,
        },
        use_sudo=True,
        use_jinja=True
    )
    sudo('systemctl enable gunicorn')
    sudo('systemctl restart gunicorn')


@task
def manage(command=""):
    with prefix('source {0}venv/bin/activate && export DATABASE_URL={1}'.format(PROJECT_DIR, DATABASE_URL)):
        with cd(DJANGO_DIR):
            run('python manage.py {0}'.format(command))


@task
def deploy():
    pull_repository()
    install_requirements()
    manage('collectstatic -c --noinput')
    manage('migrate')
    restart_service()


@task
def provision():
    upgrade_system()
    install_packages()
    setup_repository()
    create_virtualenv()
    install_requirements()
    setup_nginx()
    create_database()
    create_gunicorn_script()
    setup_systemd()
    deploy()
