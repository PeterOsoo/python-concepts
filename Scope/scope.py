'''
LEGB
Local, Enclosing, Global, Built-in
'''

for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)


# avoid using global statements
def test():
    global x

    x = 'local x'
    print(x)


test()

# Variable Scope - Understanding the LEGB rule and global/nonlocal statements


# Built-in
m = min([4, 3, 5, 2, 6, 1])
print('minimum value: ' + str(m))

# nonlocal x
# nonlocal statement used more times than global
