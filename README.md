# api_final_yatube

### Описание.

Данный проект является дополнением, расширяеющим функциональность ранее 
выполненного проекта [hw05_final](https://github.com/LariosDeen/hw05_final), 
добавляя возможность социальной сети Yatube быть интегрированной в сторонние 
приложения благодаря сервису REST API.

### Установка.

Скопируйте проект на свой компьютер:

```
git clone https://github.com/LariosDeen/api_final_yatube
```

Cоздайте и активируйте виртуальное окружение для этого проекта:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:

```
python3 manage.py migrate
```

Перейдите в директорию проекта:

```
cd yatube_api
```

Запустите проект:

```
python3 manage.py runserver
```

### Примеры.

Пользователь аутентифицируется посредвстом JWTAuthentication.
Получите токен.
Отправьте POST запрос на URL:

```
http://127.0.0.1:8000/api/v1/auth/jwt/create/
```

Получение публикаций GET запрос:

```
http://127.0.0.1:8000/api/v1/posts/
```

Создание публикации POST запрос:

```
http://127.0.0.1:8000/api/v1/posts/
```

```
{
"text": "string"
}
```

Получение одной публикации GET запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Обновление публикации PUT запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

```
{
"text": "string"
}
```

Частичное обновление публикации PATHС запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

```
{
"group": 0
}
```

Удаление публикации DELETE запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

#### Проект выполнил студент 31 когорты яндекс практикума
#### Димитри Лариос
