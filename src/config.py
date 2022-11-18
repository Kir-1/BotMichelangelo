import os
from dataclasses import dataclass


@dataclass
class Config:
    database_login: str = os.getenv('MONGODB_LOGIN')  # это логин для mongodb
    database_password: str = os.getenv('MONGODB_PASS')  # это пароль для mongodb
    url_connect: str = os.getenv('MONGODB_URI')  # ссылка для соединения с базой
    bot_token: str = os.getenv('BOT_TOKEN')  # токен бота
    name_bot: str = "t.me/michelangelo_drawer_bot" # имя бота
    url_heroku: str = "https://botmichelangelo.herokuapp.com/"
    app_name_heroku: str = os.getenv('HEROKU_APP_NAME')
    webhook_host: str = f'https://{app_name_heroku}.herokuapp.com'
    webhook_path: str = f'/webhook/{bot_token}'
    webhook_url: str = f'{webhook_host}{webhook_path}'
    webapp_host: str = '0.0.0.0'
    webapp_port: str = os.getenv('PORT', default=8000)

