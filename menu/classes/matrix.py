from typing import List, Tuple, Callable

from menu.classes.piece import Piece

class Matrix:
    def __init__(self):
        # generate the matrix
        self.grid = [
            [1] + [-2] * 10 + [1] for _ in range(4) # piece spawning area (4 rows, 10 columns + wall on each side)
        ] + [
            [1] + [0] * 10 + [1] for _ in range(22) # game area (22 rows, 10 columns + wall on each side)
        ] + [
            [1] * 12 # bottom wall (1 row, 10 columns + wall on each side)
        ]

        self.last_grid = [
            column.copy() for column in self.grid
        ]

        self.last_legal = [
            column.copy() for column in self.grid
        ]

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
    def illegal(self):
        """
        Check if the piece is illegal, if so, return True.
        :return:
        """
        return any(2 in row for row in self.grid)

    def loose(self):
        """
        Check if the game is over, if so, return True.
        :return:
        """
        return any(-1 in row for row in self.grid)

    def check_full(self) -> int:
        """
        Check if a row is full, if so, delete it and move all rows above it down, and add a new row between the piece spawning area and the game area.
        :return: the number of rows deleted
        """
        removed = 0

        for row_number in range(len(self.grid)):
            if self.grid[row_number] == [1] * 12 and row_number != 26:
                removed += 1
                del self.grid[row_number]
                self.grid.insert(4, [1] + [0] * 10 + [1])

        return removed

    def check_move(self) -> bool:

        if self.illegal():

            self.grid = [
                   column.copy() for column in self.last_legal
            ]

            return False

        else:

            self.last_legal = [
                column.copy() for column in self.grid
            ]

            self.grid = [
                column.copy() for column in self.last_grid
            ]

            return True

    def rotate(self, piece):
        """
        Rotate the piece, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """
        piece.rotate()
        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.grid = [
                column.copy() for column in self.last_legal
            ]

            piece.unrotate()

            return is_accepted, 0, self.game_matrix()

        return is_accepted, self.check_full(), self.game_matrix()

    def horizontal(self, function: Callable) -> Tuple[bool, int, List[List[int]]]:
        """
        Move the piece horizontally, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move
        :return: if the move has been accepted, the number of rows deleted, and the game matrix.
        """

        function()

        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.grid = [
                column.copy() for column in self.last_legal
            ]
            return is_accepted, 0, self.game_matrix()

        return is_accepted, self.check_full(), self.game_matrix()

    def right(self, piece):
        """
        Move the piece right, if the move is illegal, then the piece is placed at the last legal position.
        :param piece:
        :return:
        """
        accepted, count, matrix = self.horizontal(piece.right)

        if not accepted:
            piece.left()

        return accepted, 0, self.game_matrix()

    def left(self, piece):
        """
        Move the piece left, if the move is illegal, then the piece is placed at the last legal position.
        :param piece:
        :return:
        """
        accepted, count, matrix = self.horizontal(piece.left)

        if not accepted:
            piece.right()

        return accepted, 0, self.game_matrix()

    def play(self, piece) -> Tuple[bool, int, List[List[int]]]:
        """
        Play a move, if the move is illegal, then the piece is placed at the last legal position.
        :param piece: the piece to move
        """
        # either Piece.down , Piece.left or Piece.right
        piece.down()

        is_accepted = self.check_move()

        if not is_accepted:
            # the grid is now the last legal grid
            self.last_grid = [
                column.copy() for column in self.grid
            ]

        return is_accepted, self.check_full(), self.game_matrix()
        # return if the move has been accepted, the number of rows deleted, and the game matrix.


    def game_matrix(self):
        """
        Remove the walls, ceiling and floor from the matrix.
        :return:
        """

        to_return = []

        for row_index in range(4, 26):
            to_return.append(self.last_legal[row_index][1:11])

        return to_return