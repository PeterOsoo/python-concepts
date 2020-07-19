class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Developer(Employee):
    pass


emp_1 = Employee('Rateng', 'Daddy', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

dev_1 = Developer('Ondiek', 'Ondiek', 90000)

print(emp_1.email)
print(dev_1.pay)
