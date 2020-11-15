class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 23, 67000)
e2 = Employee('Ondiek', 32, 23400)
e1 = Employee('Ratego', 54, 45800)


employees = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e.sort, reverse=True)
# s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)
