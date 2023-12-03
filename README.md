# <p align="center"> Spotify </p>

#
![Example Image](x_images/spotify.png)


## Контакты

Вопросы и обратная связь: [kutmanvip01@gmail.com](mailto:ваш_email)


## Статус проекта
В режиме отладки 

[![Build Status](ссылка_на_бейдж)](ссылка_на_статус)


## Ссылки

- [Документация](ссылка_на_документацию)
- [Демонстрационный сайт](ссылка_на_сайт)


## Установка

1. Склонируйте репозиторий: `git clone https://github.com/ваш_репозиторий.git`
2. Открыть ту папку в PyCharm 
3. Установите зависимости: `pip3 install -r requirements.txt`
4. crate database 
5. crate superuser 
6. Работа с миграциями:
   6. +      1)Cоздаем файл миграции
                 python3 manage.py makemigrations
      +      2)Запускаем файл миграции
                 python3 manage.py migrate


### .env 
1. DB_NAME= ""
2. DB_USER=""
3. DB_PASSWORD=" "
4. DB_HOST=localhost
5. DB_PORT=5432
6. DEBUG=True
7. ALLOWED_HOSTS=localhost 127.0.0.1
8. EMAIL_USER= " "

9. EMAIL_PASSWORD= ***
10. SECRET= from settings.py


## Запуск

Запустите проект командой: `python manage.py runserver`