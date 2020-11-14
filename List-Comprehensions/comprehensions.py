# List Comprehensions 

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)

print([n for n in nums])

# I want 'n*n' for each 'n' in nums

my_list = []
for n in nums:
  my_list.append(n*n)
print(my_list)

# my_list = [n * n for n in nums]


# Using a map + lambda
# map runs everything in list through a certain function 
# lambda is an anonymous function 
my_list = map(lambda n: n*n, nums)
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# create list of only even numbers 
my_list = []
for n in nums:
  if n%2 == 0:
    my_list.append(n)
print(my_list)

# Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter,num))
print(my_list)

# simpler way 
# value in bracket have to match 
# complicated list 
mylist = [(letter, num) for  letter in 'abcd' for num in range(4) ]
print(my_list)
