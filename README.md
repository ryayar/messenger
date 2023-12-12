# Мессенджер  
Небольшой мессенджер на [Django](https://www.djangoproject.com/) (backend) и [Nuxt.JS](https://nuxt.com/) (Frontend).\
Нет никакого шифрования сообщений.

Используется стандартная БД sqlite для хранения пользователей и сообщений, так же переопределена модель хранения пользователей, добалены новые поля, которых нет в стандартной модели.

---
Скачать и установить Python и Node.JS\
[Python](https://www.python.org/downloads/release/python-381/) - 3.8.1\
[Node.JS](https://nodejs.org/en/blog/release/v18.18.0) - 18.18.0
---
#### Загрузить ветку
```bash
git clone https://github.com/ryayar/messenger.git
```

#### Виртуальное окуружение
```bash
python -m venv .venv # создать виртуальное окуружение
./.venv/Scripts/activate # запустить виртуальное окуружение
```

#### Установить зависимости
```
cd backend # перейти в каталог backend
pip install -r req.txt # установить зависимости для Python

cd ../frontend # перейти в каталог frontend
npm install # установить зависимости для Nuxt.JS
```
---
В первом терминале
```bash
npm run dev # запуск Nuxt.JS
```
Открыть второй терминал и перейти в каталог backend
```sh
python manage.py runserver # запуск сервера Django
```
---
### Cервер Django
`http://127.0.0.1:8000` 
### Cервер Nuxt.JS
`http://localhost:3000`

Страница регистрации и авторизации

`http://localhost:3000/login`