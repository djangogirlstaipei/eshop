# Django 實戰
自己的購物網站自己做

### Requirements

- Python 3.5+
- Django 1.10+


## Course Slides

[第一堂 - 商品管理](http://www.slideshare.net/flywindy/django-69634386)

[第二堂 - 版本管理（本次課程使用 Git-it 教學）](http://jlord.us/git-it/index-zhtw.html)

[第三堂 - 商品呈現](https://www.dropbox.com/s/nz0rvcrdpg9qga5/class_based_view.pdf?dl=0)

[第四堂 - 雲端部署](https://dl.dropboxusercontent.com/u/3991557/Django%20Deployment.pdf)

[第五堂 - 前端美化](https://www.dropbox.com/s/76ruiqc5unzb38k/EShop%20Bootstrap.pdf?dl=0)

[第六堂 - 會員管理](https://app.box.com/s/6z6q1odrft6sbhbi8ptirnmsv92sn9q7)


## How to connect us
taipei@djangogirls.org


## Getting Started

### Set up a Virtual Environment

#### Built-in `venv`

（Windows）

	python -m venv VENV
	VENV\Scripts\activate


（Linux / OS X）

	python3 -m venv VENV
	source VENV/bin/activate


#### [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org)

You need to specify your python path when creating the virtual environment:

    mkvirtualenv --python=$(which python3) eshop


### Install Django

Use pip:

    pip install django


### Get Ready for Development

`cd` into the `bookshop` directory:

    cd bookshop

And migrate the database:

    python manage.py migrate

Now you’re all set!

### Run the Development Server

    python manage.py runserver

Then you can open the website: [http://localhost:8000/](http://localhost:8000/)


### Enter the Django Admin

To log in, you need to create a superuser:

	python manage.py createsuperuser

After setup the username and password, you can login: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Deployment

* [Deploy to heroku](HEROKU.md)
* [Deploy to self-hosted server](DEPLOY.md)

