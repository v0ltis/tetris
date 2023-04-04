from tools import cnf_load as config
from datetime import datetime
import requests

class server:
    def __init__(self) -> None:
        cnf = config.load()

        self.host = cnf['server']['host']

    def send_stats(self, name: str, score: int, date: datetime, gamemode: int, duration: datetime):
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
        if not 0 < count < 51:
            raise ValueError("Count must be between 1 and 50")
        
        data = {
            "count": count,
            "starting": starting,
            "gamemode": gamemode
        }

        return requests.get(self.host + "/api/get", data=data).json()
    
    