# Yamdb_final - финальный проект 16 спринта

![workflow](https://github.com/vawy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Технологии
Python 3.7
Dajngo 2.2.16 - framework
Gunicorn 20.0.4 - http server
PostgreSQL - DB

### Шаблон наполнения env-файла
SECRET_KEY=wedvg!23_245dffgttddc345...
DB_ENGINE=django.db.backends.postgresql
DB_NAME=dbname
POSTGRES_USER=username
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=1234

### Развертка и запуск проекта
ssh mforcourses@178.154.224.46
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

### IP 
178.154.224.46


