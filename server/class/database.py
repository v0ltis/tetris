import mysql.connector
from datetime import datetime

class Database:
    def __init__(self, host:str, database:str, user:str, password:str) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._db = database

        self._cursor = None

    def execute(self, request, params):
        self._cursor.execute(request, params)
        self._conn.commit()

    def connect(self):
        self._conn = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            database = self._db
        )

        self._cursor = self._conn.cursor()

    def add_score(self, name:str, score:int, date:datetime):
        self.execute("INSERT INTO scores (name, score, date) VALUES (%s, %s, %s)", (name, score, date))


db = Database(
    host = "beryllium.cloud.voltis.me",
    database="s12_tetris",
    user="u12_iKk3mX4DKW",
    password="7sbhV.P7mGQwPwkxISKQTC^n"
).connect()

   

