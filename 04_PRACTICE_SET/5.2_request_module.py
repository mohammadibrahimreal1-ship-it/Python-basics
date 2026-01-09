import requests # pip install requests -> make sure you runned this (as it's external module)

r = requests.get("https://api.github.com")
print(r.json())