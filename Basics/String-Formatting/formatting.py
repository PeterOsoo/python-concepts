person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

# placeholder
# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

# for values need repeat
# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(
    person['name'], person['age'])
print(sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(
#     name='Jenn', age='30')
# print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
