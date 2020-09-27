# delay


import requests


r = requests.get('http://httpbin.org/delay/1',
                 timeout=3)

print(r)
