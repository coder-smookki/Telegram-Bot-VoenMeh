# Telegram-Bot-VoenMeh
Telegram bot for the Ustinov BSTU Voenmekh University. The bot will help you for different purposes.


### Запуск

1. Запуск без миграций:
   ```bash
   docker-compose up --build
   ```
   
2. Запуск с миграциями:
   ```bash
   docker-compose up --build
   ```
   В другой консоли:
   ```bash
   cd ./src
   alembic revision --autogenerate 
   ```
   Перезапустить докер, чтобы миграции прошли