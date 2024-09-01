#!/usr/bin/env python3

class Movie:
    def __init__(self,
                 title: str,
                 director: str,
                 release_year: int,
                 genre: str,
                 rating: float) -> None:
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.rating = rating

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if isinstance(value, str):
            self.__title = value
        else:
            raise TypeError('Title must be a string.')

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, value: str) -> None:
        if isinstance(value, str):
            self.__director = value
        else:
            raise TypeError('Director must be a string.')

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, value: int) -> None:
        if isinstance(value, int) and 1888 <= value <= 2100:
            self.__release_year = value
        else:
            raise ValueError('Release year must be an integer between 1888 and 2100.')

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, value: str) -> None:
        if isinstance(value, str):
            self.__genre = value
        else:
            raise TypeError('Genre must be a string.')

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, value: float) -> None:
        if isinstance(value, float) and 0.0 <= value <= 10.0:
            self.__rating = value
        else:
            raise ValueError('Rating must be a float between 0.0 and 10.0.')

    def __str__(self) -> str:
        return (f"Movie's title: {self.title}\n"
                f"Director: {self.director}\n"
                f"Release Year: {self.release_year}\n"
                f"Genre: {self.genre}\n"
                f"Rating: {self.rating:.1f}/10")