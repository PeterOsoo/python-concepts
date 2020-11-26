import re

urls = '''
https://www.google.com
http://ratengd.com
https://youtube.com
https://www.nasa.gov
'''

# add groups
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(2))
