# Duck Typing and Easier to ask forgiveness than permission (EAFP)


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    # pass
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    try:
        thing.quack()
        thing.fly()

        # add bark method that doesn't exist
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
