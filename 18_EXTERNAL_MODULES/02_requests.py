import requests 

r = requests.get('https://api.github.com/users/mdrayan001')

with open("18_EXTERNAL_MODULES\mdrayan.text","w") as f:
    f.write(r.text)