# SCHOOL PROJECT

This Project is using python version `3.8` 

# THIS PROJECT STACKS
1. Django Rest Framework
2. Drf Nested Routers
3. Django


## TO INSTALL PROJECT
1. Install pipenv on your local
2. Run `pipenv install` on project level


## TO START PROJECT
1. Create `.env` file and put your credential there needed credential are: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
2. Run `/manage.py showmigrations` to check table that will be created
3. Run `/manage.py makemigrations` to make sure you have the latest migration script
4. Run `/manage.py migrate` to create database object on your database
5  Run `./manage.py runserver or python manage.py runserver` to start server and visit http://127.0.0.1:8000/


## TO RUN TEST SCRIPT
1. run `pytest --cov=.`


## EDGE CASES
1. Error Handling still not correct





