#!/usr/bin/env python3
import datetime
import validators
from typing import Tuple

class Person:
    def __init__(self, firstname: str,
                 lastname: str,
                 birthdate: Tuple[int, int, int],
                 email: str,
                 address: str = 'Somewhere in Egypt') -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.address = address

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        if isinstance(value, str):
            self.__firstname = value
        else:
            raise TypeError('First name must be a string.')

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        if isinstance(value, str):
            self.__lastname = value
        else:
            raise TypeError('Last name must be a string.')

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        if isinstance(value, str):
            self.__address = value
        else:
            raise TypeError('Address must be a string.')

    @property
    def birthdate(self) -> str:
        return self.__birthdate.strftime("%x")

    @birthdate.setter
    def birthdate(self, value: Tuple[int, int, int]) -> None:
        if isinstance(value, tuple) and len(value) == 3 and all(isinstance(val, int) for val in value):
            try:
                year, month, day = value
                self.__birthdate = datetime.datetime(year, month, day)
            except ValueError as e:
                raise ValueError(f'Invalid date: {e}')
        else:
            raise ValueError('Birthdate must be a tuple of three integers (year, month, day).')

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if isinstance(value, str):
            if validators.email(value):
                self.__email = value
            else:
                raise ValueError('Invalid email format.')
        else:
            raise TypeError('Email must be a string.')

    @property
    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def __str__(self) -> str:
        return (f"Person's Name: {self.fullname}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Address: {self.address}\n"
                f"Email: {self.email}")