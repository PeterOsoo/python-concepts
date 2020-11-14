
# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip function creates a list of tuples 
print(zip(names, heros))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)


my_dict = {name: hero for name, hero in zip (names, heros)}
print(my_dict)


# add restrictions 
# If name not equal to Peter
my_dict = {name: hero for name, hero in zip (names, heros) if name != 'Peter'}
print(my_dict)

# comprehentions make it easy to add loops and conditionals 
