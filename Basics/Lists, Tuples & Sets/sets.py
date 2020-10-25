# Sets get rid od duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)
print('Math' in cs_courses)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# same
print(cs_courses.intersection(art_courses))

# that occur in one list
print(cs_courses.difference(art_courses))

# get all courses
print(cs_courses.union(art_courses))
