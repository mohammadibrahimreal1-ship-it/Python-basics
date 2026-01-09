'''2 types of modules in Python
-> Built-in module
-> External module
'''

import math
import os
import mymodule 
import requests

print(math.sqrt(25))        #. or dot after 'math' means I want to use a function from this module
print(mymodule.sum(2,100))
r = requests.get("https://www.google.com")
print(r.text)