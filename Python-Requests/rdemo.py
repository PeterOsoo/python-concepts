import requests

r = requests.get('https://xkcd.com/353/')

print(r)
print(dir(r))
print(help(r))

print(r.text)
print(r.status_code)
