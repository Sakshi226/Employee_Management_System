import re

from datetime import datetime

valid_id = []


def validate_emp_id(emp_id):
    if emp_id not in valid_id:
        valid_id.append(emp_id)
        return True
    else:
        return False


def valid_name(name):
    l = name.split()
    if len(l) == 3:
        if l[0].isalpha() and l[1].isalpha() and l[2].isalpha():
            return True
    return False


def valid_departments(department):
    valid_department = {"hr", "finance", "it", "marketing", "sales", "operations"}
    if department.lower() in valid_department:
        return True
    return False


def valid_designation(designation):
    valid_designations = {"vice president", "ceo", "manager", "executive director", "finance manager"}
    if designation.lower() in valid_designations:
        return True
    return False


def valid_salary(salary):
    if salary.isdigit():
        return True
    return False


def valid_mobile_no(mobile_no):
    if len(mobile_no) == 10 and mobile_no.isdigit():
        return True
    return False


def aadhar_number(adhar_number):
    if len(adhar_number) == 12 and adhar_number.isdigit():
        return True
    return False


# import re
def validate_pan_no(pan_no):
    expression = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(expression, pan_no):
        return True
    return False


# # user_date = input("enter the date(YYYY-MM-DD): ")


# def valid_dob(year, month, date):
#     year, month, date = map(int, year, month, date.split('-'))
#     if year < 0:
#         return False
#
#     if month < 1 or month > 12:
#         return False
#     if month in {1, 3, 5, 7, 8, 10, 12} and (date < 1 or date > 31):
#         return False
#     elif month in {4, 6, 9, 11} and (date < 1 or date > 30):
#         return False
#     elif month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             if date < 1 or date > 29:
#                 return False
#         else:
#             if date < 1 or date > 28:
#                 return False
#     return True


# if valid_dob(year, month, date):
#     current_year = datetime.now().year
#     age = current_year - year
#     print(f"the year is : {year, month, date},{age}")
# else:
#     print("invalid date")


# user_doj = input("enter date of joining ")
# year, month, date = map(int, user_doj.split('-'))




def validate_gender(gender):
    valid_gender = ["male", "female", "other"]
    if gender.lower() in valid_gender:
        return True
    else:
        return False


def validate_city(state, city):
    valid_state_city = {"Maharashtra": ["Pune", "Mumbai", "Jalgaon", "Dhule", "Nasik"],
                        "Madhya Pradesh": ["Burhanpur", "Indore", "Ujjain"], "Andhra Pradesh": ["Tirupati"]}
    v = valid_state_city[state]
    if city in v:
        return True
    else:
        return False
