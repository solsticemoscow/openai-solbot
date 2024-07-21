

import requests

url = "https://api.vectara.io/v2/corpora/:corpus_key/query"

payload={}
headers = {
  'Accept': 'application/json',
  'x-api-key': 'zwt_UA2fb6jB-GWYqP0NaLLjC6TIDNQqMP0-K95Rzw'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
