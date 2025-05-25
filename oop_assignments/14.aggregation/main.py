# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    def display_info(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"
class Department:
    def __init__(self, dept_name, employee:Employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_department_info(self):
        return f"Department: {self.dept_name}, Employee: {self.employee.display_info()}"
    
emp1 = Employee(101, "Ayesha")

dept1 = Department("HR", emp1)

print(dept1.show_department_info())
