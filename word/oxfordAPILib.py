# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

app_id = '20197d9e'
app_key = '37c40d1f9204a09cc68ade4864bd5733'
#base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/'

language = 'en'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/registers=Technical;domains=Computing'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
jsonRes = r.json()

# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))