#!/usr/bin/env python3
from typing import List

class Meal:
    def __init__(self, 
                 name: str, 
                 ingredients: List[str], 
                 calories: int) -> None:
        self.name = name
        self.ingredients = ingredients
        self.calories = calories

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string.")

    @property
    def ingredients(self) -> List[str]:
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: List[str]) -> None:
        if isinstance(value, list) and all(isinstance(ingredient, str) for ingredient in value):
            self.__ingredients = value
        else:
            raise TypeError("Ingredients must be a list of strings.")

    @property
    def calories(self) -> int:
        return self.__calories

    @calories.setter
    def calories(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__calories = value
        else:
            raise ValueError("Calories must be a non-negative integer.")

    def __str__(self) -> str:
        ingredients_list = ', '.join(self.ingredients)
        return (f"Meal's Name: {self.name}\n"
                f"Ingredients: {ingredients_list}\n"
                f"Calories: {self.calories} kcal")