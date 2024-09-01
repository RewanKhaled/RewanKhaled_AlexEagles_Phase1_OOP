#!/usr/bin/env python3
import sys
import re
from typing import Tuple, Optional
from models.airline import Airline
from .person import Person
from helpers.fixed_values import allowed_airlines
from helpers.helper_functions import map_range

# Convert allowed airlines to lowercase for validation
lower_value_allowed_airlines = list(map(str.lower, allowed_airlines))

class Employee(Person):
    def __init__(self, 
                 firstname: str,
                 lastname: str,
                 birthdate: Tuple[int],
                 email: str,
                 start_hour: str,
                 finish_hour: str,
                 salary: int,
                 airline: Airline,
                 address: str = 'Somewhere in Egypt') -> None:
        super().__init__(firstname, lastname, birthdate, email, address)
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.salary = salary
        self.airline = airline

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        if isinstance(value, int) and value >= 5000:
            self.__salary = value
        else:
            raise ValueError('Salary must be an integer and at least 5000.')

    @property
    def airline(self) -> Airline:
        return self.__airline

    @airline.setter
    def airline(self, value: Optional[Airline]) -> None:
        if value is None or isinstance(value, Airline):
            self.__airline = value
        else:
            raise TypeError('Airline must be an Airline object or None.')

    @property
    def start_hour(self) -> str:
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, value: str) -> None:
        if isinstance(value, str) and re.match(r'^\d{1,2}:\d{2} (PM|AM)$', value):
            self.__start_hour = value
        else:
            raise ValueError('Start hour must be in the format "HH:MM AM/PM".')

    @property
    def finish_hour(self) -> str:
        return self.__finish_hour

    @finish_hour.setter
    def finish_hour(self, value: str) -> None:
        if isinstance(value, str) and re.match(r'^\d{1,2}:\d{2} (PM|AM)$', value):
            self.__finish_hour = value
        else:
            raise ValueError('Finish hour must be in the format "HH:MM AM/PM".')

    @property
    def working_hours(self) -> str:
        start_time, start_period = self.__start_hour.split(' ')
        finish_time, finish_period = self.__finish_hour.split(' ')
        start_hour, start_minute = map(int, start_time.split(':'))
        finish_hour, finish_minute = map(int, finish_time.split(':'))

        # Convert 12-hour time format to 24-hour format
        start_hour += 12 if start_period == 'PM' and start_hour != 12 else 0
        finish_hour += 12 if finish_period == 'PM' and finish_hour != 12 else 0
        start_hour -= 12 if start_period == 'AM' and start_hour == 12 else 0
        finish_hour -= 12 if finish_period == 'AM' and finish_hour == 12 else 0

        # Calculate working hours
        working_hours = finish_hour - start_hour + (finish_minute - start_minute) / 60
        hours = int(working_hours)
        minutes = int((working_hours - hours) * 60)
        return f'{hours}:{minutes:02d} Hours'

    def salary_raise(self, value: int) -> None:
        if isinstance(value, int):
            self.__salary += value
        else:
            raise TypeError("Salary raise must be an integer.")

    def __str__(self) -> str:
        return (f"Employee's Start Hour: {self.start_hour}\n"
                f"Finish Hour: {self.finish_hour}\n"
                f"Salary: {self.salary}\n"
                f"Working Hours: {self.working_hours}\n"
                f"Airline: {self.airline.airline_name if self.airline else 'None'}")