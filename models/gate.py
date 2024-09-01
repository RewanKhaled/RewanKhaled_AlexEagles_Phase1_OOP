#!/usr/bin/env python3
from typing import Tuple

class Gate:
    def __init__(self,
                 gate_number: int,
                 gate_location: str,
                 gate_allowed_passing_people: int,
                 gate_size: Tuple[int, int]) -> None:
        self.gate_number = gate_number
        self.gate_location = gate_location
        self.gate_allowed_passing_people = gate_allowed_passing_people
        self.gate_size = gate_size

    @property
    def gate_number(self) -> int:
        return self.__gate_number

    @gate_number.setter
    def gate_number(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__gate_number = value
        else:
            raise ValueError('Gate number must be an integer greater than or equal to 0.')

    @property
    def gate_location(self) -> str:
        return self.__gate_location

    @gate_location.setter
    def gate_location(self, value: str) -> None:
        if isinstance(value, str):
            self.__gate_location = value
        else:
            raise TypeError('Gate location must be a string.')

    @property
    def gate_allowed_passing_people(self) -> int:
        return self.__gate_allowed_passing_people

    @gate_allowed_passing_people.setter
    def gate_allowed_passing_people(self, value: int) -> None:
        if isinstance(value, int) and value >= 2:
            self.__gate_allowed_passing_people = value
        else:
            raise ValueError('The number of allowed passing people must be an integer greater than or equal to 2.')

    @property
    def gate_size(self) -> Tuple[int, int]:
        return self.__gate_size

    @gate_size.setter
    def gate_size(self, value: Tuple[int, int]) -> None:
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(dim, int) for dim in value):
            self.__length, self.__width = value
            self.__gate_size = value
        else:
            raise ValueError('Gate size must be a tuple of two integers.')

    @property
    def length(self) -> int:
        return self.__length

    @property
    def width(self) -> int:
        return self.__width

    def __str__(self) -> str:
        return (f"Gate's Number: {self.gate_number}\n"
                f"Gate's Location: {self.gate_location}\n"
                f"Max Allowed People: {self.gate_allowed_passing_people}\n"
                f"Gate's Size: {self.gate_size} (Length: {self.length}, Width: {self.width})")