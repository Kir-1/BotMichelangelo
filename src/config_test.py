import os
from dataclasses import dataclass


@dataclass
class ConfigTest:
    database_login: str = "Kir-1"  # это логин для mongodb
    database_password: str = "WhnI78irLr9pifkg"  # это пароль для mongodb
    url_connect: str = f"mongodb+srv://Kir-1:{database_password}@cluster0.xxveor0.mongodb.net/?retryWrites=true&w" \
                       f"=majority"  # ссылка для соединения с базой
    bot_token: str = "5675525258:AAH4COiDs5HEsoKPuP-RP_ln6T6VInQFpHA"  # токен бота
    name_bot: str = "t.me/michelangelo_drawer_bot"  # имя бота
