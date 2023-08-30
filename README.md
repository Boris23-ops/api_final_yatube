# Проект API Yatube.

## Описание проекта
Позволяет создавать, читать, изменять и удалять свои посты, а так же читать чужие посты и подписываться на их авторов посредством API-запросов.

## Технологии
•	Python 3.9
•	Django==3.2.3
•	djangorestframework==3.12.4
•	JWT + Djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### После запуска сервера вам будет доступна документация
>http://127.0.0.1:8000/redoc


###4jui Примеры запросов 

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

`GET http://127.0.0.1:8000/api/v1/posts/`

Ответ:

```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {}
    ]
}
```

Добавление новой публикации в коллекцию публикаций от авторизованного пользователя 

`POST http://127.0.0.1:8000/api/v1/posts/`

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Ответ:

```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```


### Автор
[Короткиян Борис](https://github.com/Boris23-ops)