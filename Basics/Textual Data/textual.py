message = 'Hello World'

print(message[9])

# first index is inclusive
print(message[2:9])
print(message[:9])
print(message[6:])


# methods
print(message.upper())
print(message.lower())
print(message.count('l'))
print(message.find('World'))


new_message = message.replace('World', 'Universe')

print(new_message)


greeting = 'Hello'
name = "Michael"

message = greeting + ', ' + name + '. Welcome!'

message2 = '{}, {}. Welcome! '.format(greeting, name)

# fstring
message3 = f'{greeting}, {name.upper()}. Welcome! '
print(message)
print(message2)
print(message3)


#  what methods available
print(dir(name))
print(help(str))
print(help(str.lower()))
