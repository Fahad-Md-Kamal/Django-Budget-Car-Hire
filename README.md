# Django-Budget-Car-Hire

## Dependencies
* django
* pillow
* django-bootstrap4
* django-crispy-forms
* faker
* stripe
* reportlab
* psycopg2

## Database Engine
* PostGreSql

## Contanirization
* Docker
* Docker-compose

> Install python, Docker and docker-compose.

*python: https://www.python.org/downloads/*
*Docker: https://get.docker.com/*
*docker-compose: https://docs.docker.com/compose/install/*

Go into the project directory. Open Terminal and type: 
```sudo docker-compose build```
(This may take some time since the images are big files)
Now type: 
```sudo docker-compose up``` if fails stop the process and run the command again. After that open new Terminal on the same directory and typ : ```sudo docker-compose run python bash``` You are now into the Docker container bash. Now type:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
If you want to load sidding data type this command into the docker container bash:
```python seeder_data.py```
This will load some fake data for you to observe. If it fails in the middle of loading fake data don't penic. This is not a major issue.

**Congratulations !!** You can brows the site on your local matchin by browning:
```
localhost:8000
```