from pydantic import BaseModel
"""
This file contains the classes that represent the body shape required for API requests.
When a default value is specified, this value will be used if none is specified in the request.
"""


class GetUserStats(BaseModel):
    """
    The requestBody of the GET request for user stats
    """
    username: str
    gamemode: str = "all"
    quantity: int
    offset: int = 0


class GetScores(BaseModel):
    """
    The body of the GET request for scores
    """
    quantity: int
    offset: int = 0
    gamemode: str = "all"


class PostScores(BaseModel):
    """
    The body of the POST request for scores
    """
    name: str
    score: int
    date: float
    gamemode: str
    duration: int
