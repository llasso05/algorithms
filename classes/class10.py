"""Create a Manager class that tracks employees using a dictionary.

Implement add_employee(id, name), remove_employee(id), and list_employees()."""

# Manager class
class Manager:
    def __init__(self):
        self.employees = {} # dictionary

# add employee
    def add_employee(self,id, employee):
        self.employees[id] = employee

# remove employee
    def remove_employee(self, id):
        if id in self.employees:
            del self.employees[id]

    def list_employees(self):
        # list employees
        print(self.employees)


m = Manager()
m.add_employee(101, "Alice")
m.add_employee(102, "Bob")
m.list_employees()  # Should print both employees
m.remove_employee(101)
m.list_employees()  # Should print only Bob
