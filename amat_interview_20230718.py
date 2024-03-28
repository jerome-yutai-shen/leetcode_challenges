# -*- coding: utf-8 -*-
"""
Created on Jul 18 11:50:29 2023

@author: Jerome Yutai Shen

write a code which give gender wise employee count from IT department who have age is less than 45

"""
import datetime
from enum import Enum, unique


@unique
class Gender(Enum):
    female = 1
    male = 2


@unique
class Department(Enum):
    dep1 = 1
    dep2 = 2
    dep3 = 3
    IT = 4


class Employee:
    """
    Obj for a single unique employee
    """

    def __init__(self, id: str, name: str, date_of_birth: datetime, gender: Gender, department: Department):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.department = department


def count_employees(all_employees: list, gender_wise: Gender, department: Department, age_range: int):
    count = 0

    for employee in all_employees:
        age = (datetime.datetime.now() - employee.date_of_birth).total_seconds()/3600/24/365
        if employee.gender == gender_wise and employee.department == department and age <= 45:
            count += 1
    return count



if __name__ == "__main__":
    all_employees_input_list = [["01", "john", datetime.datetime(1990,1,1), Gender(2), Department(1)],
                                ["03", "andy", datetime.datetime(1992,1,3), Gender(2), Department(2)],
                                ["05", "anne", datetime.datetime(1972,1,1), Gender(1), Department(3)],
                                ["12", "lily", datetime.datetime(1978,9,1), Gender(1), Department(4)]]
    all_employees = []
    for _ in all_employees_input_list:
        assert len(_) == 5 #
        employee = Employee(*_) # simply add * befor the list _ to unpack
        all_employees.append(employee)

    print(count_employees(all_employees, Gender(1), Department["IT"], 45))

