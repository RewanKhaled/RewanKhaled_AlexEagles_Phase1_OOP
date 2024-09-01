#!/usr/bin/env python3
from typing import List, Union
from .employee import Employee
from .meal import Meal
from .movie import Movie
from helpers.fixed_values import allowed_airlines


class Airline:
    def __init__(self, airline_name: str, employees: List[Employee], services: List[Union[Movie, Meal]]) -> None:
        self.airline_name = airline_name
        self.employees = employees
        self.services = services

    @property
    def airline_name(self) -> str:
        return self.__airline_name

    @airline_name.setter
    def airline_name(self, value: str) -> None:
        if value not in allowed_airlines:
            raise ValueError('Airline name is not in the available airlines in Egypt.')
        self.__airline_name = value

    @property
    def employees(self) -> List[Employee]:
        return self.__employees

    @employees.setter
    def employees(self, value: List[Employee]) -> None:
        if value is None:
            self.__employees = []
        elif isinstance(value, list) and all(isinstance(emp, Employee) for emp in value):
            self.__employees = value
        else:
            raise TypeError('Employees should be a list of Employee objects.')

    def add_employee(self, value: Employee) -> None:
        if isinstance(value, Employee):
            self.__employees.append(value)
        else:
            raise TypeError('The value provided is not an Employee object.')

    def remove_employee(self, employee_name: str) -> None:
        if not isinstance(employee_name, str):
            raise TypeError('Employee name should be a string.')
        
        for employee in self.__employees:
            if employee.fullname == employee_name:
                self.__employees.remove(employee)
                print('Employee was found and removed.')
                return
        print("Employee wasn't found.")

    @property
    def services(self) -> List[Union[Meal, Movie]]:
        return self.__services

    @services.setter
    def services(self, value: List[Union[Meal, Movie]]) -> None:
        if value is None:
            self.__services = []
        elif isinstance(value, list) and all(isinstance(svc, (Meal, Movie)) for svc in value):
            self.__services = value
        else:
            raise TypeError('Services should be a list containing Meal or Movie objects.')

    def add_service(self, value: Union[Meal, Movie]) -> None:
        if isinstance(value, (Meal, Movie)):
            self.__services.append(value)
        else:
            raise TypeError('You should provide a Meal or Movie object.')

    def remove_service(self, service_name: str) -> None:
        if not isinstance(service_name, str):
            raise TypeError('Service name should be a string.')

        for service in self.__services:
            if (isinstance(service, Meal) and service.name == service_name) or \
               (isinstance(service, Movie) and service.title == service_name):
                self.__services.remove(service)
                print('Service was found and removed.')
                return
        print("Service wasn't found.")

    def __str__(self) -> str:
        return (f'{self.airline_name}\nEmployees Count: {len(self.employees)}\n'
                f'Available Services Count: {len(self.services)}')