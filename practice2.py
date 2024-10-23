from datetime import time


class Students:
    fees_increment = 1.04
    def __init__(self, first,second, age, course,fees):
        self.first = first
        self.second = second
        self.age = age
        self.course = course
        self.fees = fees
        self.email = first + '.' + second +'@gmail.com'

    def student_name(self):
        return f"FName:{self.first}, SName:{self.second}, Age:{self.age}, Course:{self.course}, Email:{self.email}, Fees:{self.fees}"
    def apply_raise(self):
        self.fees = int(self.fees * self.fees_increment)
        return f"Your new fees is: {self.fees}"
#     running class instances that affect the whole class and not a single entity
    @classmethod
    def set_raise_amt(cls,amount):
        cls.fees_increment = amount
        return cls
    @classmethod
    def from_timestamp(cls, timestamp):
        year, month, day, hour, minute, second = time.localtime(timestamp)
        return cls(year, month, day, hour, minute, second)

    @classmethod
    def today(cls, timestamp, _time=None):
        timestamp = _time.time()
        return cls.from_timestamp(timestamp)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        else:
            return False

stu1 = Students("James", "Gachomba", "18", "ACMP", 170000)
stu2 = Students("Faith", "Bitutu", "16", "CMP", 150000)

Students.set_raise_amt(1.35)

print(stu1.student_name())
print(stu2.student_name())
print(stu1.fees_increment)
print(Students.is_workday(1))
print(Students.today(2))


