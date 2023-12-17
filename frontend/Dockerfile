# Используем базовый образ Node.js
FROM node:latest

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json (если есть) в контейнер
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы проекта в контейнер
COPY . .

# Команда для сборки Nuxt.js проекта
RUN npm run build

# Команда для запуска сервера Nuxt.js
CMD ["npm", "run", "start"]
