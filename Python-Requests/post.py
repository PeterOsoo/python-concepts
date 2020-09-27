import requests

payload = {'username': 'ondiek', 'password': 'testing'}

r = requests.post('https://httpbin.org/post', data=payload)

# print(r.text)
# print(r.url)


# getting json response back
print(r.json())

r_dict = r.json()
print(r_dict['form'])
