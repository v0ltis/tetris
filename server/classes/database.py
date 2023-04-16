from __future__ import annotations
import mysql.connector
from datetime import datetime
import pydantic

class Database:
    def __init__(self, host:str, database:str, user:str, password:str, port:int=3306) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._db = database
        self._port = port

        self._cursor = None

    def _execute(self, request, params):
        self._cursor.execute(request, params)
        self._conn.commit()

    def _get (self, request, params):
        self._cursor.execute(request, params)
        return self._cursor.fetchall()

    def connect(self) -> Database:
        self._conn = mysql.connector.connect(
            host = self._host,
            port = self._port,
            user = self._user,
            password = self._password,
            database = self._db
        )

        self._cursor = self._conn.cursor(dictionary=True)
        return self
    
    def add_score(self, name:pydantic.constr(max_length=25), score:int, date:datetime, gamemode: int, duration: datetime) -> None:
        """
        Add a score to the database
        :param name: The name of the player. Must be between 1 and 25 characters.
        :param score: The score of the player
        :param date: The date of the score
        :param gamemode: The gamemode of the score performed
        :param duration: The time it took to complete the game
        :return:
        """
        self._execute("INSERT INTO scores (username, score, date, gamemode, duration) VALUES (%s, %s, %s, %s, %s)", (name, score, date, gamemode, duration))

    def get_scores(self, limit: pydantic.conint(ge=1, le=50), offset: pydantic.conint(ge=0) = 0) -> list[tuple[str, int, datetime]]:
        """
        Get the top scores from the database
        :param limit: The number of scores to get. Must be between 1 and 50
        :param offset: The number of scores to skip. Must be greater than or equal to 0
        :return: A list of tuples containing the name, score and date of the scores
        """
        return self._get("SELECT * FROM scores ORDER BY score DESC LIMIT %s OFFSET %s", (limit, offset))

    def get_gamemode_scores(self, gamemode: str, limit: pydantic.conint(ge=1, le=50), offset: pydantic.conint(ge=0) = 0) -> list[tuple[str, int, datetime]]:
        """
        Get the top scores from the database
        :param gamemode: The gamemode of the scores to get
        :param limit: The number of scores to get. Must be between 1 and 50
        :param offset: The number of scores to skip. Must be greater than or equal to 0
        :return: A list of tuples containing the name, score and date of the scores
        """
        return self._get("SELECT * FROM scores WHERE gamemode = %s ORDER BY score DESC LIMIT %s OFFSET %s", (gamemode, limit, offset))
