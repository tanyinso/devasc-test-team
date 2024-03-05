import requests

input = input("enter a email to look up")
key = "YOUR_API_KEY_HERE"
type = "email"
url = "https://www.ipqualityscore.com/api/json/leaked/%s/%s/%s" % (type,key,input)

x = requests.get(url).json()
if x["exposed"] == true:
    print("email was detected in leaked data")
else:
    print("email is not leaked")
