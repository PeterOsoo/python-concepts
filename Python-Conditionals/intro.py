language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match!')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credentials ')


if not logged_in:
    print('Please Log in ')


a = [1,2,3]
b = [1,2,3]

print(a is b)