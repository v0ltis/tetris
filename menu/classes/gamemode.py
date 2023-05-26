import random
import time
from typing import List

from classes.piece import Piece


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

    def __init__(self, name: str, id: int,
                 default_speed: int, speed_multiplier: float, speed_increment_every: int, max_speed: int,
                 pieces: List[Piece], invisible_pieces: bool = False, xp_multiplier: float = 1.0
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
        self.max_speed = max_speed

        self.invisible_pieces: bool = invisible_pieces
        self.pieces: List[Piece] = pieces

        self.score = 0
        self.round = 0
        self.duration = None

        self.actual_piece: Piece = random.choice(self.pieces)
        self.next_piece: Piece = random.choice(self.pieces)

        self.pause_time = None

        self.next_go_down = 0

        self.loose = False

    def start(self) -> None:
        """
        Starts the gamemode
        :return: None
        """
        self.duration = time.time()

        self.next_go_down = time.time() + (0.4 + 1 / self.speed)

    def next_round(self) -> None:
        """
        Invoked after each round
        Updates the speed if needed
        Updates the actual and next piece
        :return: None
        """

        self.round += 1

        if self.round % self.speed_increment_every == 0:
            self.speed *= self.speed_multiplier

            if self.speed > self.max_speed:
                self.speed = self.max_speed

        # reset x & y pointers.
        self.actual_piece.reset()
        self.actual_piece = self.next_piece
        self.next_piece = random.choice(self.pieces)

    def get_time(self) -> float:
        """
        Returns the time elapsed since the gamemode started
        :return: float
        """
        return time.time() - self.duration
    
    def get_score(self) -> int:
        """
        Returns the score
        :return: int
        """
        return self.score

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

        # + 0.4 seconds in order to not penalise the player after pausing
        self.next_go_down = time.time() + (0.8 + 1 / self.speed)

    def should_go_down(self) -> bool:
        """
        Returns if the piece should go down
        :return: bool
        """
        go_down = time.time() > self.next_go_down

        if go_down is True:
            # if true, set the next go down time.
            self.next_go_down = time.time() + 1 / self.speed

        # return if the piece should go down.
        return go_down

    def add_score(self, rows):
        """
        Add points depending on the number of rows deleted

        0 rows = 0 points
        1 row = 40 points
        2 rows = 100 points
        3 rows = 300 points
        4 rows = 1200 points
        :param rows:
        :return:
        """

        self.score += {
            0: 0,
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }[rows]
