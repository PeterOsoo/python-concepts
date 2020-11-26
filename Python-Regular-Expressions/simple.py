import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
ratengd.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# r for raw string
# pattern = re.compile(r'abc')

# pattern = re.compile(r'ratengd\.com')

pattern = re.compile(r'\d\d\d.\d\d\d[-.]\d\d\d\d')


pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])


# span is beginning and end index of match
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')


with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
