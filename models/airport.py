#!/usr/bin/env python3
import sys
import datetime
from typing import Tuple, List

sys.path.append("..")
from helpers.fixed_values import not_allowed_items_in_airports
from .employee import Employee
from .gate import Gate


class Airport:
    not_allowed_items_in_airports = not_allowed_items_in_airports

    def __init__(self, 
                 airport_name: str,
                 airport_location: str,
                 airport_date_of_construction: Tuple[int, int, int],
                 gates: List[Gate], 
                 employees: List[Employee],
                 airport_size: Tuple[int, int],
                 wifi_availability: bool = True):
        self.airport_name = airport_name
        self.airport_location = airport_location
        self.airport_date_of_construction = airport_date_of_construction
        self.gates = gates
        self.airport_size = airport_size
        self.employees = employees
        self.wifi_availability = wifi_availability

    @property
    def airport_name(self) -> str:
        return self.__airport_name

    @airport_name.setter
    def airport_name(self, value: str) -> None:
        if isinstance(value, str):
            self.__airport_name = value
        else:
            raise TypeError('Airport name must be a string.')

    @property
    def airport_location(self) -> str:
        return self.__airport_location

    @airport_location.setter
    def airport_location(self, value: str) -> None:
        if isinstance(value, str):
            self.__airport_location = value
        else:
            raise TypeError('Airport location must be a string.')

    @property
    def airport_date_of_construction(self) -> str:
        return self.__airport_date_of_construction.strftime("%x")

    @airport_date_of_construction.setter
    def airport_date_of_construction(self, value: Tuple[int, int, int]) -> None:
        if isinstance(value, tuple) and len(value) == 3 and all(isinstance(v, int) for v in value):
            year, month, day = value
            self.__airport_date_of_construction = datetime.datetime(year, month, day)
        else:
            raise ValueError('Date of construction must be a tuple of three integers (year, month, day).')

    @property
    def gates(self) -> List[Gate]:
        return self.__gates

    @gates.setter
    def gates(self, value: List[Gate]) -> None:
        if isinstance(value, list) and all(isinstance(g, Gate) for g in value):
            self.__gates = value
        else:
            raise TypeError('Gates must be a list of Gate objects.')

    def add_gate(self, gate: Gate) -> None:
        if isinstance(gate, Gate):
            self.__gates.append(gate)
        else:
            raise TypeError('To add a gate, you must provide a Gate object.')

    def remove_gate(self, gate_number: int) -> None:
        if isinstance(gate_number, int):
            gate_to_remove = next((g for g in self.__gates if g.gate_number == gate_number), None)
            if gate_to_remove:
                self.__gates.remove(gate_to_remove)
                print('Gate was found and removed.')
            else:
                print("Gate wasn't found.")
        else:
            raise TypeError('Gate number must be an integer.')

    @property
    def airport_size(self) -> Tuple[int, int]:
        return self.__airport_size

    @airport_size.setter
    def airport_size(self, value: Tuple[int, int]) -> None:
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(v, int) for v in value):
            self.__airport_size = value
        else:
            raise ValueError('Airport size must be a tuple of two integers (length, width).')

    @property
    def employees(self) -> List[Employee]:
        return self.__employees

    @employees.setter
    def employees(self, value: List[Employee]) -> None:
        if isinstance(value, list) and all(isinstance(emp, Employee) for emp in value):
            self.__employees = value
        else:
            raise TypeError('Employees must be a list of Employee objects.')

    def add_employee(self, employee: Employee) -> None:
        if isinstance(employee, Employee):
            self.__employees.append(employee)
        else:
            raise TypeError('To add an employee, you must provide an Employee object.')

    def remove_employee(self, employee_name: str) -> None:
        if isinstance(employee_name, str):
            employee_to_remove = next((emp for emp in self.__employees if emp.fullname == employee_name), None)
            if employee_to_remove:
                self.__employees.remove(employee_to_remove)
                print('Employee was found and removed.')
            else:
                print("Employee wasn't found.")
        else:
            raise TypeError('Employee name must be a string.')

    @property
    def wifi_availability(self) -> bool:
        return self.__wifi_availability

    @wifi_availability.setter
    def wifi_availability(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__wifi_availability = value
        else:
            raise TypeError('WiFi availability must be a boolean.')

    def __str__(self) -> str:
        return (f'Airport Name: {self.airport_name}\n'
                f'Location: {self.airport_location}\n'
                f'Date of Construction: {self.airport_date_of_construction}\n'
                f'Gates Count: {len(self.gates)}\n'
                f'Size (Length x Width): {self.airport_size}\n'
                f'Employees Count: {len(self.employees)}\n'
                f'WiFi Availability: {"Available" if self.wifi_availability else "Not Available"}')