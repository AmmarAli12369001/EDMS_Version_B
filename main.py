import datetime
import pickle
import os


def addEmployee():
    fullName = input("Enter full name: ")
    employeeID = int(input("Enter employee ID: "))
    department = input("Enter department: ")
    doj = input("Enter date of joining (MM/DD/YYYY): ")
    salary = int(input("Enter annual salary: "))

#loop until you get full name
    if len(fullName) == 0:
        print("Please enter full name.")
        return

    if not 10000 <= employeeID <= 99999:
        print("Employee ID should be in the range of 10000 and 99999.")
        return

    if department not in ["Marketing", "Finance", "Human Resource", "Technical"]:
        print("Department should be Marketing, Finance, Human Resource, or Technical.")
        return

    try:
        datetime.datetime.strptime(doj, "%m/%d/%Y")
    except ValueError:
        print("Invalid date of joining format.")
        return

    if not 30000 <= salary <= 200000:
        print("Salary should be in the range of 30000 and 200000.")
        return

    if not os.path.exists("employees.pkl"):
        employees = []
        with open("employees.pkl", "wb") as f:
            pickle.dump(employees, f)

    with open("employees.pkl", "rb") as f:
        employees = pickle.load(f)
        if employeeID in employees:
            print("Employee with ID1 {} already exists.".format(employeeID))
            return

    employees.append({
        "fullName": fullName,
        "employeeID": employeeID,
        "department": department,
        "doj": doj,
        "salary": salary
    })

    with open("employees.pkl", "wb") as f:
        pickle.dump(employees, f)

    print("Employee added successfully.")


def displayEmployees():
    with open("employees.pkl", "rb") as f:
        employees = pickle.load(f)

    if len(employees) == 0:
        print("No employees found.")
        return

    print("Employees:")
    for employee in employees:
        print(employee)


def deleteEmployee():
    employeeID = int(input("Enter employee ID to delete: "))

    with open("employees.pkl", "rb") as f:
        employees = pickle.load(f)
        if employeeID not in employees:
            print("Employee with ID {} does not exist.".format(employeeID))
            return

    employees.remove({"employeeID": employeeID})

    with open("employees.pkl", "wb") as f:
        pickle.dump(employees, f)

    print("Employee deleted successfully.")


def updateEmployee():
    employeeID = int(input("Enter employee ID to update: "))

    with open("employees.pkl", "rb") as f:
        employees = pickle.load(f)
        if employeeID not in employees:
            print("Employee with ID {} does not exist.".format(employeeID))
            return

    updatedSalary = None
    updatedDepartment = None

    print("What do you want to update?")
    #complete

def menu():
    print("1 to Add Employee")
    print("2 to Delete Employee")
    print("3 to Update Employee")
    print("4 to Display Employees")
    print("5 to Exit")

    ch = int(input("Enter your Choice:"))
    if ch == 1:
        addEmployee()
    elif ch == 2:
        deleteEmployee()
    elif ch == 3:
        updateEmployee()
    elif ch == 4:
        displayEmployees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Input")
        menu()


menu()
if __name__ =="__main__":
    menu()