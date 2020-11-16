import datetime

my_date = datetime.datetime(2020, 11, 16, 7, 35, 45)

print(my_date)

# November 16, 2020

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# November 16, 2020 fell on a Monday and was the 321 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
    my_date)

print(sentence)
