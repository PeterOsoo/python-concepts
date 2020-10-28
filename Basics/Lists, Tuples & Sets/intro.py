

# student = {'name': 'Jack', 'age': 25}

# print(student.get('courses'))


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)


# is keyword
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)


# while loop
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
