for i in range(1, 11):
    # two digits
    sentence = 'The value is {:02}'.format(i)
    print(sentence)


pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)

# two decimal places
print(sentence)


sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
# , separated
print(sentence)
