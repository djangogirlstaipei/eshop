# Django 實戰
自己的購物網站自己做

### Requirements

- Python 3.5+
- Django 1.10+


## Slide

[第一堂 - 商品管理](http://www.slideshare.net/flywindy/django-69634386)


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