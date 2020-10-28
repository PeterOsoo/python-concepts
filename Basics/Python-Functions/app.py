def hello_func(greeting, name="You"):
    return '{}, {} '.format(greeting, name)


print(hello_func('Hi', name="Rateng"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Klaus', age=22)


# courses = ['Math', 'Art']
# args and kwargs unpack values
