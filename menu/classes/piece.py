class Piece:
    def __init__(self, color, matrix):
        self.color = color
        self.x = 5
        self.y = 0

        self.matrix = matrix

        self.shape = [
            [1, 1, 1],
            [0, 1, 0]
        ]


    def down(self) -> None:
        """
        Move the piece down, if it can't move down, then it is placed in the matrix.
        :return: None
        """
        # increment the y coordinate of the piece
        self.y += 1

        # add the piece to the matrix at coords
        # piece shape can be 4x1 , 3x2, 2x3 or 1x4 matrix
        # coords are the coordinates of the top left corner of the piece

        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x]

    def right (self) -> None:
        """
        Move the piece right.
        :return: None
        """
        self.x += 1

        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x]

    def left (self) -> None:
        """
        Move the piece left.
        :return: None
        """
        self.x -= 1

        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x]

    def rotate(self) -> None:
        """
        Rotate the piece of 90 degrees to the right, and update the matrix.
        :return: None
        """
        """
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] -= self.shape[y][x]
        """
        self.shape = list(zip(*self.shape[::-1]))

        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x]

    def unrotate(self) -> None:
        """
        Rotate the piece of 90 degrees to the left, and update the matrix.
        :return: None
        """

        self.shape = list(zip(*self.shape))[::-1]

        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                self.matrix.grid[self.y + y][self.x + x] += self.shape[y][x]
