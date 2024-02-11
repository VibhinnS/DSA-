# data and functions of specific class are called attributes and methods
# functions - methods ; data - attr
# class is blueprint for creating instances
def main():
    class Employee:
        raise_amount = 1.04
        no_of_employee = 0

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'
            Employee.no_of_employee += 1

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

        @classmethod
        def set_raise_amt(cls, amount):
            cls.raise_amount = amount

        # alternate constructor for the class
        @classmethod
        def string_parse(cls, emp_str):
            first, last, pay = emp_str.split('-')
            return cls(first, last, pay)

        @staticmethod
        def is_workday(day):
            if day.weekday == 5 or day.weekday == 6:
                return False
            return True

    emp1 = "v-s-20000"
    emp2 = "a-b-40000"

    new_emp1 = Employee.string_parse(emp1)
    new_emp2 = Employee.string_parse(emp2)

    print(new_emp1.first)


if __name__ == "__main__":
    main()
