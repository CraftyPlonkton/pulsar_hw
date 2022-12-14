### Как запустить проект на тестовом сервере:
<details><summary> Linux </summary>

Клонировать репозиторий и перейти в папку с проектом:
```
git clone git@github.com:CraftyPlonkton/pulsar_hw.git
```
```
cd pulsar_hw/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:


```
pip install -r pulsar_hw/requirements.txt
```

Выполнить миграции:

```
python3 pulsar_hw/manage.py migrate
```
Создать и заполнить данные суперпользователя:
```
python3 pulsar_hw/manage.py createsuperuser
```

Запустить сервер:

```
python3 pulsar_hw/manage.py runserver
```

</details>

<details><summary> Windows (BASH)</summary>

Клонировать репозиторий и перейти в папку с проектом:
```
git clone git@github.com:CraftyPlonkton/pulsar_hw.git
```
```
cd pulsar_hw/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r pulsar_hw/requirements.txt
```

Выполнить миграции:

```
python pulsar_hw/manage.py migrate
```
Создать и заполнить данные суперпользователя:
```
python pulsar_hw/manage.py createsuperuser
```

Запустить сервер:

```
python pulsar_hw/manage.py runserver
```

</details>

Записи в базу данных можно внести через админ панель (вход с данными суперпользователя)
```
http://127.0.0.1:8000/admin/
```
Список товаров доступен по адресу
```
http://127.0.0.1:8000/items/
```
Страница отдельного товара
```
http://127.0.0.1:8000/items/<id>/
```
