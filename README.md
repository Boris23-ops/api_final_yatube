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


### Автор
[Короткиян Борис](https://github.com/Boris23-ops)