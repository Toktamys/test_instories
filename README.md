# **Тестовое задание от Instories**

#### Необходимые шаги для развертывания:
1. Скачать репозиторий
2. Далее, будучи в корне проекта выполнить команды <br>
`docker-compose build` <br>
`docker-compose up -d`
3. Внутри контейнера **instories_project** выполнить команду `python manage.py migrate`
4. Внутри контейнера **instories_project** выполнить команду `python manage.py createsuperuser` и создать суперпользователя
5. По адресу `127.0.0.0:8000` будет доступна админка