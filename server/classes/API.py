from pydantic import BaseModel

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
