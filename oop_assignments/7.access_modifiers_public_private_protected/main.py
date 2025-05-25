# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp =Employee("Samiya", 20000, "123-45-6789")

print("Public Variable (name): ", emp.name)  # Accessible

print("Protected Vaiable(_salary): ", emp._salary)  # Accessible, but should be treated as protected

print("Accessing Private SSN via name mangling:", emp._Employee__ssn)  # ✅ But not recommended unless necessary

