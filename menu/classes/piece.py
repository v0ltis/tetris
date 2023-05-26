from __future__ import annotations

from typing import List, TYPE_CHECKING

from copy import deepcopy

if TYPE_CHECKING:
    from classes.matrix import Matrix


class Piece:
    """
    Represents a piece Object.

    Thooses methods must NOT be called directly. Please, use the methods in the Matrix class instead.

    :param color: the color of the piece
    :param shape: the shape of the piece
    :param matrix: the matrix of the game
    """

    def __init__(self, color, shape: List[List[int]], matrix: Matrix):
        self.color = color

        self.x = 5
        self.y = 0

        self.matrix = matrix

        self.shape = shape

        # the shape of the piece when displayed in the next piece area
        # this should NOT be edited
        self.display_shape = deepcopy(shape)

    def reset(self):
        self.x = 5
        self.y = 0
        self.shape = deepcopy(self.display_shape)

    def place(self, mult: int = 1) -> None:
        """
        Place the piece in the matrix. Then, the Cases of the matrix will be colored.
        :return:
        """
        # add the piece to the matrix at coords
        # piece shape can be 4x1 , 3x2, 2x3 or 1x4 matrix
        # coords are the coordinates of the top left corner of the piece
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x] * mult

                # if there is a piece in this case, we color it
                if self.shape[y][x] != 0:
                    self.matrix.grid[self.y + y][self.x + x].color = self.color

    def down(self) -> None:
        """
        Move the piece down, if it can't move down, then it is placed in the matrix.
        :return: None
        """
        # increment the y coordinate of the piece
        self.y += 1

        # place the piece in the matrix
        self.place()

    def right(self, cancel_move=False) -> None:
        """
        Move the piece right.
        :return: None
        """

        if cancel_move:
            self.place(mult=-1)

        self.x += 1

        self.place()

    def left(self, cancel_move=False) -> None:
        """
        Move the piece left.
        :return: None
        """

        if cancel_move:
            self.place(mult=-1)

        self.x -= 1

        self.place()

    def rotate(self) -> None:
        """
        Rotate the shape of 90 degrees to the right, and update the matrix.

        DO NOT CALL THIS FUNCTION DIRECTLY, USE matrix.rotate() INSTEAD.

        :return: None
        """

        self.shape = list(zip(*self.shape))[::-1]

        self.place()

    def unrotate(self) -> None:
        """
        Rotate the shape of 90 degrees to the left, and update the matrix.

        DO NOT CALL THIS FUNCTION DIRECTLY, USE matrix.rotate() INSTEAD.
        :return: None
        """

        self.place(mult=-1)

        self.shape = list(zip(*self.shape[::-1]))

        self.place()
