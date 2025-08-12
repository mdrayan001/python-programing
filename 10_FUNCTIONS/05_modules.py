# Two types of modules in Python are:
# 1.Build in Module
# 2.External Module
# List of all the built in module : https://docs.python.org/3/py-modindex.html

import math 
import os
import mymodule
import requests

print(math.sqrt(16))  # Output: 4.0
mymodule.hello() # Output: Hello from mymodule!
r = requests.get('https://api.github.com')
print(r.status_code) # Output: 200 (if the request was successful)
