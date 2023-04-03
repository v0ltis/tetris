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

    def execute(self, request, params):
        self._cursor.execute(request, params)
        self._conn.commit()

    def get (self, request, params):
        self._cursor.execute(request, params)
        return self._cursor.fetchall()

    def connect(self):
        self._conn = mysql.connector.connect(
            host = self._host,
            port = self._port,
            user = self._user,
            password = self._password,
            database = self._db
        )

        self._cursor = self._conn.cursor()

    def add_score(self, name:pydantic.constr(max_length=25), score:int, date:datetime, gamemode: int) -> None:
        """
        Add a score to the database
        :param name: The name of the player. Must be between 1 and 25 characters.
        :param score: The score of the player
        :param date: The date of the score
        :param gamemode: The gamemode of the score performed
        :return:
        """
        self.execute("INSERT INTO scores (username, score, date, gamemode) VALUES (%s, %s, %s, %s)", (name, score, date, gamemode))

    def get_scores(self, limit: pydantic.conint(ge=1, le=50)):
        """
        Get the top scores from the database
        :param limit: The number of scores to get. Must be between 1 and 50
        :return: A list of tuples containing the name, score and date of the scores
        """
        return self.get("SELECT * FROM scores ORDER BY score DESC LIMIT %s", (limit,))
