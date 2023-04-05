import time
from typing import List

from menu.classes.piece import Piece


class Gamemode:
    """
    Represents a gamemode Object.

    :param name: The name of the gamemode
    :param id: The id of the gamemode
    :param default_speed: The default speed of the gamemode
    :param speed_multiplier: The speed multiplier
    :param speed_increment_every: How many rounds before the speed is incremented

    :param pieces: The pieces of the gamemode
    :param invisible_pieces: If, once the piece is placed, it should become invisible
    """
    def __init__(self, name:str, id:int,

                 default_speed:int, speed_multiplier:float, speed_increment_every:int,

                 pieces:List[Piece],invisible_pieces:bool=False
                 ):
        """
        Creates & setup a gamemode
        :param name: The name of the gamemode
        :param id: The id of the gamemode
        :param default_speed: The default speed of the gamemode
        :param speed_multiplier: The speed multiplier
        :param speed_increment_every: How many rounds before the speed is incremented
        :param pieces: The pieces of the gamemode
        :param invisible_pieces: If, once the piece is placed, it should become invisible
        """

        self.name = name
        self.id = id
        self.speed = default_speed
        self.speed_multiplier = speed_multiplier
        self.speed_increment_every = speed_increment_every

        self.invisible_pieces = invisible_pieces
        self.pieces = pieces

        self.score = 0
        self.round = 0
        self.duration = None


    def start(self) -> None:
        """
        Starts the gamemode
        :return: None
        """
        self.duration = time.time()

    def next_round(self) -> None:
        """
        Invoked after each round
        Updates the speed if needed
        :return: None
        """

        self.round += 1

        if self.round % self.speed_increment_every == 0:
            self.speed *= self.speed_multiplier

    def get_time(self) -> float:
        """
        Returns the time elapsed since the gamemode started
        :return: float
        """
        return time.time() - self.duration

    def pause(self) -> None:
        """
        Pauses the gamemode
        :return: None
        """
        self.pause_time = time.time()

    def resume(self) -> None:
        """
        Resumes the gamemode
        :return: None
        """
        self.duration += time.time() - self.pause_time
