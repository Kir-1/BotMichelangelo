import os

from pymongo import MongoClient
from pymongo.database import Database
from src.config import Config
#from src.config_test import ConfigTest
from dataclasses import dataclass


@dataclass
class AdminsDB:
    cluster: MongoClient = MongoClient(Config.url_connect)  # кластер
    database: Database = cluster["information"]  # база данных
    collection = dict = database["admins"]  # таблица пользователей
    password: str = os.getenv('ADMIN_PASS')  # пароль для получения админки


@dataclass
class UsersDB:
    cluster: MongoClient = MongoClient(Config.url_connect)  # кластер
    database: Database = cluster["information"]  # база данных
    collection = dict = database["users"]  # таблица пользователей


@dataclass
class LutDB:
    cluster: MongoClient = MongoClient(Config.url_connect)  # кластер
    database: Database = cluster["information"]  # база данных
    collection = dict = database["LUT"]  # таблица лутов


