# Процесс запуска бота

1. Необходимо переименовать файл ```.env.dist``` в ```.env``` *(можно создать пустой файл с именем ```.env``` и скопировать в него содержимое файла ```.env.dist```)* и указать в нем список администраторов (пользователей с повышенными правами) бота и токен, полученный при создании бота в чате с [BotFather](https://t.me/BotFather) ботом.
   
   В этом же файле можно задать начальные значения пределов показаний датчиков (температура и влажность воздуха, влажность почвы), период получения даных с датчиков (в секундах) и имя файла базы данных:

   ```dotenv
   ADMINS=1234567,1234567,1234567
   
   BOT_TOKEN=bot_token
   
   DATABASE_PATH=database.sqlite
   
   SENSORS_TIMEOUT_REQUEST=60
   
   MIN_AIR_TEMP=25
   MAX_AIR_TEMP=34
   
   MIN_AIR_HUM=40
   MAX_AIR_HUM=80
   
   MIN_GROUND_HUM=40
   MAX_GROUND_HUM=80
   ```
2. Установить все необходимые для работы бота модули из файла ```requirements.txt```, например, следующей командой:

    ```bash
   pip install -r requirements.txt
   ```
3. Запустить бота путем выполнения команды:

    ```bash
   python bot.py
   ```
