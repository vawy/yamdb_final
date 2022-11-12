# Описание
Проект YaMDB - собирает отзывы пользователей на различные произведения

![workflow](https://github.com/vawy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg) 

### Технологии
Django 2.2.16
DRF 3.12.4
Python 3.7
Gunicorn 20.0.4
PostgreSQL


### Развертка и запуск проекта локально

#### Клонирование репозитория
Клонировать репозиторий и перейти в него в командной строке:

`
git clone git@github.com:vawy/yamdb_final.git
cd api_yamdb
`

#### Изменение файлов
1) Поменять в docker-compose.yaml
    web:
      image: ../api_yamdb
2) Добавить .env в корень проекта

#### Запуск проекта
`
cd infra/
docker-compose -d --build
`

#### Миграции проекта, добавление юзера, сбор статики
`
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
`

P.s. Добавить `winpty` при ошибке:
`
the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'
`
    
### API
Документация API доступна по следующему эндпоинту:

    http://<project_ip>/redoc

#### Регистрация
Для регистрации отправьте POST-запрос на эндпоит `api/v1/auth/signup/`, в теле запроса укажите:
```JSON
{
    "username": "your_username",
    "email": "your_email"
}
```
При успешной регистрации сервер вернет данные с кодом 200.
Далее ~~на указанный электронный адрес~~ в папке sent_emails директории проекта будет лог-файл эмитирующий электронное письмо. В нем указан верификационный ключ, его необходимо сохранить для дальнейшего получения JWT-токена
#### Получение JWT-токена
Для получения JWT-токена, отправьте POST-запрос на эндпоит `api/v1/auth/token/`, в теле запроса укажите:
```JSON
{
    "username": "your_username",
    "confirmation_code": "your_code"
}
```
на энипоинт:

В ответ API вернёт JWT-токен
~~~JSON
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODU1Mzc3LCJqdGkiOiJkY2EwNmRiYTEzNWQ0ZjNiODdiZmQ3YzU2Y2ZjNGE0YiIsInVzZXJfaWQiOjF9.eZfkpeNVfKLzBY7U0h5gMdTwUnGP3LjRn5g8EIvWlVg"
}
~~~

`token` - Сам JWT-токен
Токен используется в заголовке запроса под ключом `Bearer`


## Автор

### Василий Вигилянский 

##### IP
`178.154.224.46`
