student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))

for key, value in student.items():
    print(key, value)


# add new entry to dictionary
# if key exits it will update value
student['phone'] = '222-2222'
student['name'] = 'Ondiek'
print(student.get('phone', 'Not Found'))
print(student)


student.update({'name': ' Japap', 'age': 34})
print(student)

del student['age']
print(student)


print(student.keys())
