from pymongo import MongoClient
from pymongo.database import Database
from src.config import Config
from dataclasses import dataclass


@dataclass
class AdminsDB:
    cluster: MongoClient = MongoClient(Config.url_connect)  # кластер
    database: Database = cluster["information"]  # база данных
    collection = dict = database["admins"]  # таблица пользователей
    password: str = "0000" # пароль для получения админки


@dataclass
class UsersDB:
    cluster: MongoClient = MongoClient(Config.url_connect)  # кластер
    database: Database = cluster["information"]  # база данных
    collection = dict = database["users"]  # таблица пользователей

