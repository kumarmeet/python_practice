from enum import Enum
from uuid import uuid4

from pydantic.v1 import UUID4


class Designations(Enum):
    MANAGER = "manager"
    STAFF = "staff"
    HR = "HR"
    SOFTWARE_DEVELOPER = "software_developer"


class Employee:
    count: int = 0

    __name: str
    __salary: float
    __emp_id: UUID4
    __designation: Designations

    def __init__(self, name: str, salary: float, designation: Designations):
        self.__name = name
        self.__salary = salary
        self.__emp_id = uuid4()
        self.__designation = designation
        Employee.count += 1

    def employee_details(self):
        print("Name ->", self.__name, end="\n")
        print("Salary ->", self.__salary, end="\n")
        print("Id ->", self.__emp_id, end="\n")
        print("Designation ->", self.__designation, end="\n")

    @classmethod
    def total_emp(cls):
        return cls.count


emp1 = Employee("Meet Kumar", 4444444, Designations.SOFTWARE_DEVELOPER)
emp2 = Employee("John", 94585, Designations.SOFTWARE_DEVELOPER)

emp1.employee_details()
emp2.employee_details()

print("Employee count -> ", Employee.total_emp())
