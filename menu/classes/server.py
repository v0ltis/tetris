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

    def send_stats(self, name: str, score: int, date: datetime, gamemode: int, duration: datetime) -> None:
        """
        Send the stats to the server

        :param name: The name of the player
        :param score: The score of the player
        :param date: The date of the game
        :param gamemode: The ID of the gamemode
        :param duration: The duration of the game
        :return: None
        """
        if not 0 < len(name) < 26:
            raise ValueError("Name must be between 1 and 25 characters long")

        data = {
            "name": name,
            "score": score,
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "gamemode": gamemode,
            "duration": duration.strftime("%H:%M:%S")
        }

        requests.post(self.host + "/api/submit", data=data)

    def get_stats(self, count:int, starting:int, gamemode:int = -1):
        """
        Get the stats from the server
        :param count: The number of stats to get (between 1 and 50)
        :param starting: The starting index (0 is the first)
        :param gamemode: The gamemode to get the stats from (-1 for al)
        :return:
        """
        if not 0 < count < 51:
            raise ValueError("Count must be between 1 and 50")
        
        data = {
            "count": count,
            "starting": starting,
            "gamemode": gamemode
        }

        return requests.get(self.host + "/api/get", data=data).json()
    
    