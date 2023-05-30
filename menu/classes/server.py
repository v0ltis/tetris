from tools import cnf_load as config
from datetime import datetime
import requests


class Server:
    """
    Represents the server Object

    Allows to send and get stats from the server
    host can be changed in the config.yml file
    """
    def __init__(self) -> None:
        cnf = config.load()

        self.host = cnf['server']['host']

    def send_stats(self, name: str, score: int, date: datetime, gamemode: str, duration: int) -> bool:
        """
        Send the stats to the server

        :param name: The name of the player
        :param score: The score of the player
        :param date: The date of the game
        :param gamemode: The ID of the gamemode
        :param duration: The duration of the game
        :return: bool, corresponding to the success of the request
        """
        if not 0 < len(name) < 26:
            raise ValueError("Name must be between 1 and 25 characters long")

        data = {
            "name": name,
            "score": score,
            "date": datetime.timestamp(date),
            "gamemode": gamemode,
            "duration": duration
        }

        try:
            req = requests.post(self.host + "/scores", json=data)

            if req.status_code != 202:
                return False
            else:
                return True

        except requests.exceptions.ConnectionError as e:
            return False

    def get_stats(self, quantity: int, offset: int, gamemode: str = "all"):
        """
        Get the stats from the server
        :param quantity: The number of stats to get (between 1 and 50)
        :param offset: The starting index (0 is the first)
        :param gamemode: The gamemode to get the stats from
        :return:
        """
        if not 0 < quantity < 51:
            raise ValueError("Count must be between 1 and 50")
        
        data = {
            "quantity": quantity,
            "offset": offset,
            "gamemode": gamemode
        }

        try:
            resp = requests.get(self.host + "/scores", json=data)

            if resp.status_code != 200:
                return False

            else:
                return resp.json()

        except requests.exceptions.ConnectionError:
            return False

    