import re

urls = '''
https://www.google.com
http://ratengd.com
https://youtube.com
https://www.nasa.gov
'''

# add groups
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))
