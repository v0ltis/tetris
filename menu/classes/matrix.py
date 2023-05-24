from typing import List, Tuple, Callable, TYPE_CHECKING

from classes.matrix_case import Case

from classes.piece import Piece

from copy import deepcopy

class Matrix:
    """
    Represents a matrix Object.

    It is the central part of the game. It contains the grid, and all the pieces.
    It also contains the methods to move the pieces, and to check if the pieces can move.

    You can safely use the methods of this class to move the pieces.

    Be aware of the retuned values of the methods, they are used to check if the piece can move.
    If a piece is marked as "placed", it means that it can't move anymore. Moving it again could (and would) cause an index error.
    """
    def __init__(self):
        # generate the matrix
        self.grid = self._constructor()

        self.last_grid = self._constructor()

        self.last_legal = self._constructor()

        """
        Matrix looks like this:
        
        [ 1 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2  1 ]
        [... 2 more rows ...]
        [ 1 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2  1 ]
        [ 1  0  0  0  0  0  0  0  0  0  0  1 ]
        [... 20 more rows ...]
        [ 1  0  0  0  0  0  0  0  0  0  0  1 ]
        [ 1  1  1  1  1  1  1  1  1  1  1  1 ] # bottom wall, no piece can go below this.
        """

    # static method means we do not ask for the "self" element.
    # "self" will not be given by python to the function.
    @staticmethod
    def _constructor() -> List[List[Case]]:
        """
        Generate the matrix. Could not use comprehensions because Case() would be duplicated over the lines.
        :return: the matrix
        """
        matrix = []
        for i in range(4):
            # generate the piece spawning area with walls on each side
            matrix.append([Case(1)] + [Case(-2) for _ in range(10)] + [Case(1)])

        for i in range(22):
            # generate the game area with walls on each side
            matrix.append([Case(1)] + [Case(0) for _ in range(10)] + [Case(1)])

        # generate the floor
        matrix.append([Case(1) for _ in range(12)])

        return matrix


    def _print(self):
        """
        Print the matrix.
        """
        for row in self.last_legal:
            print(row)

    def illegal(self):
        """
        Check if the piece is illegal, if so, return True.
        If there is a 2, it means there was a 1+1 performed, which means a piece try
                    to go through another piece or the wall or floor wich is illegal.
        :return: True if the piece is illegal, False otherwise
        """
        if any(2 in row for row in self.grid) : print("ATTENTION")
        return any(2 in row for row in self.grid)

    def loose(self):
        """
        Check if the game is over, if so, return True.
        If there is a -1, it means there was a -2+1 performed, which means a placed piece is overlapping in the spawning
        area wich means the game is over.
        :return: True if the game is over, False otherwise
        """
        return any(-1 in row for row in self.grid)

    def check_full(self) -> int:
        """
        Check if a row is full, if so, delete it and move all rows above it down, and add a new row between the piece spawning area and the game area.
        Called after a piece is placed and marked as a valid move.
        Called: self.horizontal(), self.down(), self.rotate()
        :return: the number of rows deleted
        """
        removed = 0

        for row_number in range(len(self.grid)):
            if all(case.value == 1 for case in self.grid[row_number]) and row_number != 26:
                removed += 1
                del self.grid[row_number]
                self.grid.insert(4, [Case(1)] + [Case(0)] * 10 + [Case(1)])

        return removed

    def check_move(self) -> bool:
        """
        Check if the move is legal, if so, return True and update the last legal grid.
        If the move is illegal, return False and update the grid to the last legal grid.
        :return: True if the move is legal, False if the move is illegal.
        """
        if self.illegal():

            self.grid = deepcopy(self.last_legal)

            return False

        else:

            self.last_legal = deepcopy(self.grid)

            self.grid = deepcopy(self.last_grid)

            return True

    def rotate(self, piece: Piece) -> Tuple[bool, int, List[List[Case]]]:
        """
        Rotate the piece, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move
        :return: if the rotation has been accepted, the number of rows deleted, and the game matrix.
        """
        piece.rotate()
        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.grid = deepcopy(self.last_legal)

            piece.unrotate()

            return is_accepted, 0, self.game_matrix()

        return is_accepted, self.check_full(), self.game_matrix()

    def horizontal(self, function: Callable) -> Tuple[bool, int, List[List[Case]]]:
        """
        Move the piece horizontally, if the move is illegal, then the piece is placed at the last legal position.

        DO NOT CALL THIS FUNCTION DIRECTLY, USE self.right() OR self.left() INSTEAD.

        :param function: Represent the function that allow to the piece to turn. Either piece.left or piece.right without the ()
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """

        function()

        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.grid = deepcopy(self.last_legal)

            return is_accepted, 0, self.game_matrix()

        return is_accepted, self.check_full(), self.game_matrix()

    def right(self, piece: Piece) -> Tuple[bool, int, List[List[Case]]]:
        """
        Move the piece right, if the move is illegal, then the piece is placed at the last legal position.
        :param piece:
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """
        accepted, count, matrix = self.horizontal(piece.right)

        if not accepted:
            piece.left()

        return accepted, 0, self.game_matrix()

    def left(self, piece: Piece):
        """
        Move the piece left, if the move is illegal, then the piece is placed at the last legal position.
        :param piece:
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """
        accepted, count, matrix = self.horizontal(piece.left)

        if not accepted:
            piece.right()

        return accepted, 0, self.game_matrix()

    def down(self, piece: Piece) -> Tuple[bool, int, List[List[Case]]]:
        """
        Move the piece down, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move

        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        Note: IF FALSE HAS BEEN RETURNED, DO NOT TRY TO MOVE THE PIECE DOWN AGAIN, IT WILL CAUSE AN ERROR.
        """
        # either Piece.down , Piece.left or Piece.right
        piece.down()

        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.grid = deepcopy(self.last_legal)

        return is_accepted, self.check_full(), self.game_matrix()
        # return if the move has been accepted, the number of rows deleted, and the game matrix.

    def drop(self, piece: Piece) -> Tuple[bool, int, List[List[Case]]]:
        """
        Drop the piece, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """
        while not self.check_move():
            piece.down()

        self.last_grid = deepcopy(self.grid)

        return True, self.check_full(), self.game_matrix()

    def game_matrix(self) -> List[List[Case]]:
        """
        Remove the walls, ceiling and floor from the matrix.
        :return: the game matrix without the walls, ceiling and floor.
        """

        to_return = []

        for row_index in range(4, 26):
            to_return.append(self.last_legal[row_index][1:11])

        return to_return