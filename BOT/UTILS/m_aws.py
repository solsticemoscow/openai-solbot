import requests


result = requests.get(url='https://92psbce97k.execute-api.eu-north-1.amazonaws.com/default/openai')

print(result)



import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../../FILES/gapps-336903-firebase-adminsdk-k8i4t-6235b04ce0.json")
firebase_admin.initialize_app(cred)
