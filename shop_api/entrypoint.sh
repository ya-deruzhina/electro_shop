#!/bin/bash
# pipenv run python manage.py register_periodic_tasks
pipenv run python manage.py migrate 
pipenv run python manage.py runserver 0.0.0.0:8000
exit