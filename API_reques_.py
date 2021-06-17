import json
import requests
from pprint import pprint

# post_code_req = requests.get("https://api.postcodes.io/postcodes/eh74nn")

# print(post_code_req.status_code)
# print(post_code_req.headers)
# pprint(post_code_req.text)
# pprint(post_code_req.content)
# pprint(post_code_req.json())

json_body = json.dumps({'postcodes': ['PR30SG', 'M456GN', 'EX165BL']})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

pprint(post_multi_req.json())
