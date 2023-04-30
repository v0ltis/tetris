from __future__ import annotations

# A matrix case is a kind of int that can be used to represent a case in the matrix,
# but also contain the color of the piece that is in this case.
from typing import Tuple

# allow to copy every objects
from copy import deepcopy


class Case:
    def __init__(self, value: int = 0, color: Tuple[int, int, int] = (0, 0, 0)):
        self.value = value
        self.color = color

    def __int__(self) -> int:
        """
        __int__ is called when int() is used.
        :return:
        """
        return self.value

    def __add__(self, other) -> Case:
        """
        __add__ is called when + is used.

        :param other:
        :return:
        """
        if isinstance(other, Case):
            return Case(self.value + other.value, self.color)
        else:
            return Case(self.value + other, self.color)

    def __iadd__(self, other) -> Case:
        """
        __iadd__ is called when += is used.

        :param other:
        :return:
        """
        if isinstance(other, Case):
            self.value += other.value
        else:
            self.value += other
        return self

    def __sub__(self, other) -> Case:
        """
        __sub__ is called when - is used.

        :param other:
        :return:
        """
        if isinstance(other, Case):
            return Case(self.value - other.value, self.color)
        else:
            return Case(self.value - other, self.color)

    def __isub__(self, other) -> Case:
        """
        __isub__ is called when -= is used.
        :param other:
        :return:
        """
        if isinstance(other, Case):
            self.value -= other.value
        else:
            self.value -= other
        return self

    def __repr__(self) -> str:
        """
        __repr__ is called when repr() is used.
        :return:
        """
        return f'{self.value}'

    def __str__(self) -> str:
        """
        __str__ is called when str() is used.
        :return:
        """
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        if isinstance(other, Case):
            return self.value == other.value
        else:
            return self.value == other

    def _copy(self):
        return Case(self.value, deepcopy(self.color))
