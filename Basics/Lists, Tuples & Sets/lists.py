# lists
courses = ['History', 'Math', 'Physics', 'CompSci']

# print(list_1)

# loop through the list
for course in courses:
    print(course)

# index
print(courses[0])

# get last item
print(courses[-1])

# length of lists
print(len(courses))


# slicing
print(courses[0:2])
print(courses[:3])
print(courses[1:])


# list methods
# add item to list to end use append, insert at index

courses.append('Art')
courses.insert(0, 'PE')

print(courses)

courses_2 = ['Education', 'Drawing']
# courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses.extend(courses_2)
print(courses)


courses.remove('Math')
popped = courses.pop()
print(courses)
print(popped)


courses.reverse()
print(courses)

# sort lists
nums = [1, 4, 2, 3, 5]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# using sorted function
sorted_nums = sorted(nums)
print(sorted_nums)


print(min(nums))
print(sum(nums))
print(max(nums))


print(courses.index('PE'))

print('Index in courses......')
for index, course in enumerate(courses, start=1):
    print(index, course)


course_str = ','.join(courses)
print(course_str)
course_str = ' - '.join(courses)
print(course_str)

# to return new list
new_list = course_str.split(' - ')
print(new_list)
