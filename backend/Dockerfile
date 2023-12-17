# Используем базовый образ Python
FROM python:3.8.1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt update
RUN apt upgrade -y
RUN apt install -y python3-dev
RUN apt install -y gcc
# Копируем requirements.txt в контейнер
COPY req.txt .

# Устанавливаем зависимости
RUN pip install -r req.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Команда для запуска Django сервера
CMD ["python", "manage.py", "runserver"]
