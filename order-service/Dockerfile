# Используем базовый образ Python на базе Alpine
FROM python:3.8-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости и очищаем кэши
RUN pip install --no-cache-dir -r requirements.txt

# Определяем команду для запуска приложения
ENTRYPOINT [ "python" ]
CMD ["app.py" ]