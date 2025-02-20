class Company:
    # class attribute
    company_name = "TechCorp"

    def __init__(self, name, position):
        # attributes
        self.name = name
        self.position = position

    def show_details(self):
        print(f"Employee name:{self.name}, position:{self.position}")

e1 = Company("John", "Developer")
e2 = Company("Emma", "Designer")

e1.show_details()
e2.show_details()
print(Company.company_name)  # Should be "TechCorp"
