
import requests


r = requests.get('http://httpbin.org/basic-auth/ondiek/testing',
                 auth=('ondiek', 'testing'))

print(r.text)
