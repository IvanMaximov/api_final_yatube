# API_YATUBE
## Описание

API_YATUBE позволяет неавторизованным пользователям получать информацию
о постах, группах и комментариях. Авторизованные пользователи могут 
создавать, изменять или удалять свои посты и комментарии. Также 
авторизованные пользователи могут подписываться друг на друга.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
'git clone https://github.com/IvanMaximov/api_final_yatube.git'
'cd api_final_yatube'
Cоздать и активировать виртуальное окружение:
'python3 -m venv venv'
'source venv/bin/activate'
'python3 -m pip install --upgrade pip'
Установить зависимости из файла requirements.txt:
'pip install -r requirements.txt'
Выполнить миграции:
'python3 manage.py migrate'
Запустить проект:
'python3 manage.py runserver'