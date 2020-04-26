# event-manager
Event manager project for college course

## How to run?
Make sure you are in event_manager directory using command `pwd`

And then run following command to run the server:

`python manage.py runserver`

## Requirements
Python v3+

django v2+

## Installation
To install django, run the following command:
`pip install django`

To install MySQL, use:
`pip install pymysql`

To install crispy-forms, use:
`pip install django-crispy-forms`

To check if django is installed, use:
`python -m django --version`

To check if python is installed, use:
`python --version`

## Migrations
To run migrations run the following commands in order:

`python manage.py makemigrations`

`python manage.py migrate`

## Start new app
To start a new app use:
`python manage.py startapp <app_name>`

After that add to event_manager setting.py to INSTALLED_APPS.

Started sprint 2