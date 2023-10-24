from Validate import *
from datetime import datetime


class Student:
    def __init__(self, emp_id, name, gender, mobile_no, salary, age, state, city, address, DOB, aadhar_card_no,
                 pan_card_no, department,designation):
        self.emp_id = emp_id
        self.name = name
        self.gender = gender
        self.mobile_no = mobile_no
        self.salary = salary
        self.age = age
        self.state = state
        self.city = city
        self.address = address
        self.DOB = DOB
        self.aadhar_card_no = aadhar_card_no
        self.pan_card_no = pan_card_no
        self.department = department
        self.designation = designation

    def display(self):
        print(self.emp_id, " ", self.name, " ", self.mobile_no, " ", self.gender, " ", self.salary, " ", self.age, " ",
              self.state, " ", self.city,
              " ",
              self.address, " ", self.DOB, " ", self.aadhar_card_no, " ", self.pan_card_no, " ", self.department, " ",
              self.designation)


stud = []
while True:
    print("1: Add a Record")
    print("2: Display a Record")
    print("3: Search a Record")
    print("4: Update a record")
    print("5: Exit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        while True:
            emp_id = input("Enter your emp_id : ")
            if validate_emp_id(emp_id):
                break
            else:
                print("Employee with already exist,please choose a unique id")
        while True:
            name = input("Enter name : ")
            if valid_name(name):
                break
            else:
                print("Invalid name ")
        while True:
            gender = input("Enter your gender ")
            if validate_gender(gender):
                print(gender)
                break
            else:
                print("Invalid,Enter again ")
        while True:
            salary = input("Enter your salary : ")
            if valid_salary(salary):
                print(salary)
                break
            else:
                print("Invalid,Enter numbers only")
        while True:
            state = input("Enter your state : ")
            city = input("Enter your city : ")
            if validate_city(state, city):
                break
            else:
                print("Invalid")

        while True:
            mobile_no = input("Enter your mobile number : ")
            if valid_mobile_no(mobile_no):
                break
            else:
                print("Invalid, Enter valid mobile_no: ")
        while True:
            DOB = input("Enter the date(YYYY-MM-DD) : ")
            year, month, date = map(int, DOB.split('-'))


            def valid_dob(year, month, date):
                if year < 0:
                    return False

                if month < 1 or month > 12:
                    return False
                if month in {1, 3, 5, 7, 8, 10, 12} and (date < 1 or date > 31):
                    return False
                elif month in {4, 6, 9, 11} and (date < 1 or date > 30):
                    return False
                elif month == 2:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        if date < 1 or date > 29:
                            return False
                    else:
                        if date < 1 or date > 28:
                            return False
                return True
            if valid_dob(year, month, date):
                current_year = datetime.now().year
                age = current_year - year
                print(age)
                break
            else:
                print("Invalid date,Enter the date in YYYY_MM_DD format: ")
        while True:
            department = input("Enter your department : ")
            if valid_departments(department):
                break
            else:
                print("Invalid, Enter valid number : ")
        while True:
            designation = input("Enter your designation : ")
            if valid_designation(designation):
                break
            else:
                print("Invalid, Enter valid number : ")
        while True:
            aadhar_card_no = input("Enter your aadhar_card number : ")
            if aadhar_number(aadhar_card_no):
                break
            else:
                print("Invalid, Enter valid number : ")
        while True:
            pan_card_no = input("Enter your pan_card_no number : ")
            if validate_pan_no(pan_card_no):
                break
            else:
                print("Invalid, Enter valid number : ")

        # age = int(input("Enter the age "))
        address = input("Enter your address : ")

        s = Student(f"Emp_id is: {emp_id} ", f"Name of employee is: {name} ", f"Gender is: {gender}", f"Mobile No: {mobile_no} ",
              f"Salary is : {salary} ", f"Age : {age} ", f"State: {state} ", f"city: {city} ", f"address: {address} ", f"DOB : {DOB} ",
                    f"addhar_card_no: {aadhar_card_no} ",f"pan_no: {pan_card_no} ", f"department{department} ", f"designation: {designation}")
        stud.append(s)
    elif choice == 2:
        print("Details of student")
        for i in stud:
            i.display()
    elif choice == 3:
        print("Press A to search by Employee id")
        print("Press B to search by Employee name")
        print("Press C to search by Department name")
        ch = input("enter the choice ")
        if ch == "A":
            emp_id = input("Enter the Employee id to search ")
            for i in stud:
                if i.emp_id == emp_id:
                    i.display()
        elif ch == "B":
            emp_name = input("Enter the Employee name to search ")
            for i in stud:
                if i.name == emp_name:
                    i.display()
        elif ch == "C":
            dept_name = input("Enter the Department name to search ")
            for i in stud:
                if i.department == dept_name:
                    i.display()
        else:
            print("Invalid,no such record")

    elif choice == 4:
        user_id = input("Enter the emp_id ")
        for i in stud:
            if i.emp_id == user_id:
                print(" press I to update name ")
                print(" press II to update address ")
                print(" press III to update dob ")
                ch = input("enter what you want to update")
                if ch == "I":
                    nm = input("Enter the update name: ")
                    i.name = nm
                elif ch == "II":
                    add = input("enter the updated address: ")
                    i.address = add
                elif ch == "III":
                    dob = input("enter the  updated DOB: ")
                    i.dob = dob
                elif ch == "d":
                    print("Press i to update the salary of specific employee by Employee_id.")
                    print("Press ii to update the salary of all employee working in specific department.")
                    print("Press iii to update the salary of all employee.")
                    ch = input("Enter ur choice.")
                    if ch == "i":
                        eid = input("Enter the Employee_id to update the salary.")
                        flag = True
                        for i in stud:
                            if i.emp_id == eid:
                                flag = False
                                i.sal = i.sal + i.sal * 0.1
                                print("Salary updated of the gievn Employee_id")
                        if flag == True:
                            print("Employee_id Not Found")
                    elif ch == "ii":
                        dn = input("Enter the Department_name to update the salary of all employee.")
                        flag = True
                        for i in stud:
                            if i.department == dn:
                                flag = False
                                i.salary += i.salary * 0.1
                                print("Salary updated of all employee has been updated of the given department")
                        if flag == True:
                            print("Department_name Not Found")
                    elif ch == "iii":
                        for i in stud:
                            i.salary += i.salary * 0.1
                            print("Salary updated for all employees.")
                else:
                    print("invalid choice")
    elif choice == 5:
        em_id = input("enter the emp_id to delete the record")
        for i in stud:
            if i.emp_id == em_id:
                stud.remove(i)

    elif choice == 6:
        highest_salary_list = []
        for i in stud:
            highest_salary_list.append(i.salary)
            print("Maximum salary is", max(highest_salary_list))

    elif choice == 7:
        lowest_salary_list = []
        for i in stud:
            lowest_salary_list.append(i.salary)
            print("Minimum salary is", min(lowest_salary_list))

    elif choice == 8:
        break

    else:
        print("invalid choice")
