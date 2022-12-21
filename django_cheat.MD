# Install django (~= same as 3.1.\*)

~$ pip install django~=3.1.0

# New django project (from project_name folder)

~$ django-admin startproject config .

# Create app (from project_name folder)

~$ python manage.py startapp app_name

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver => ex. http://127.0.0.1:8000

# Add app to settings.py

INSTALLED_APPS = [ … , 'app_name' ]

# App templates folder

create folder appfolder/templates/appname

# Project templates folder:

create folder projectname/templates

# settings.py template config

Project templates settings.py:
TEMPLATES = [
{ …
'DIRS': [BASE_DIR / 'templates', ],
… }

# Create Static folder:

project_name\static\

# Static folder (settings.py):

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = 'static_root'

# To use PostgresSQL

# pip install psycopg2

# settings.py

DATABASE = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'blog',
'USER': 'admin',
'PASSWORD': '123456',
'HOST': 'localhost',
'PORT': '5432'

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls), # pre-created admin urls routes
path('', include('app_name.urls')) # include your app urls
]

rom django.urls import path
from . import views

url patterns = [
path('posts', views.index, name='posts.index'),
path('posts/create/', views.create, name='posts.create',
path('posts/<int:id>/', views.show, name='posts.show'),
path('posts/<int:id>/edit/', views.edit, name='posts.edit'),
path('posts/<int:id>/delete/', views.delete, name='posts.delete'),
]
