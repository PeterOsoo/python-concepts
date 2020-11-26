import re

emails = '''
RatengOndiek@gmail.com
rateng.ondiek@university.edu
rateng-321-ondiek@my-work.net
'''


pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
