class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        self.date_of_registration = "14-12-2005"
    def dsplay_employee(self):
        print(f"Our employ is {self.name} paid: {self.salary}")
    def update_salary(self, amount):
        if amount > 0:
            self.salary += amount
            return self.salary
        else:
            print("Amount can't be negative")

employ1 = Employee("James", "10000")
employ2 = Employee("Peter", "12000")

print(employ1.salary)
employ1.dsplay_employee()
print(employ2.update_salary((100)))


