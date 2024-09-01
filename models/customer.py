#!/usr/bin/env python3
from validators import isin
from .person import Person
from .flight import Flight
from typing import Tuple, List, Optional

class Customer(Person):
    def __init__(self, 
                 firstname: str,
                 lastname: str,
                 birthdate: Tuple[int],
                 email: str,
                 budget: int,
                 flights: Optional[List[Flight]] = None,
                 address: str = 'Somewhere in Egypt') -> None:
        super().__init__(firstname, lastname, birthdate, email, address)
        self.budget = budget
        self.flights = flights if flights is not None else []

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__budget = value
        else:
            raise ValueError("Budget must be a non-negative integer.")

    @property
    def flights(self) -> List[Flight]:
        return self.__flights

    @flights.setter
    def flights(self, value: Optional[List[Flight]]) -> None:
        if value is None:
            self.__flights = []
        elif isinstance(value, list) and all(isinstance(flight, Flight) for flight in value):
            self.__flights = value
        else:
            raise TypeError("Flights must be a list of Flight objects or None.")

    def add_flight(self, flight: Flight) -> None:
        if isinstance(flight, Flight):
            self.__flights.append(flight)
        else:
            raise TypeError("Only Flight objects can be added.")

    def remove_budget(self, amount: int) -> None:
        if isinstance(amount, int) and amount >= 0:
            if amount > self.__budget:
                raise ValueError("Insufficient budget.")
            self.__budget -= amount
        else:
            raise ValueError("Amount must be a non-negative integer.")

    def add_budget(self, amount: int) -> None:
        if isinstance(amount, int) and amount >= 0:
            self.__budget += amount
        else:
            raise ValueError("Amount must be a non-negative integer.")

    def __str__(self) -> str:
        flight_ids = [flight.flight_id for flight in self.__flights]
        return (f"Customer's Name: {self.fullname}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Address: {self.address}\n"
                f"Email: {self.email}\n"
                f"Budget: {self.budget}\n"
                f"Booked Flights: {flight_ids}")