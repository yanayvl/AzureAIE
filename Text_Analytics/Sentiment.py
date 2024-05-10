import requests
# pprint is used to format the JSON response
from pprint import pprint

subscription_key = "YourKey"
endpoint = "YourEndpoint"

sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

documents = {"documents": [
    {"id": "1", "language": "en",
     "text": "I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable."},
    {"id": "2", "language": "es",
     "text": "Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)

keyphrase_url = endpoint + "/text/analytics/v3.0/keyphrases"

documents = {"documents": [
    {"id": "1", "language": "en",
     "text": "I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable."},
    {"id": "2", "language": "es",
     "text": "Si usted quiere comunicarse con Carlos, usted debe de llamarlo a su telefono movil. Carlos es muy "
             "responsable, pero necesita recibir una notificacion si hay algun problema."},
    {"id": "3", "language": "en",
     "text": "The Grand Hotel is a new hotel in the center of Seattle. It earned 5 stars in my review, and has the "
             "classiest decor I've ever seen."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(keyphrase_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)

entities_url = endpoint + "/text/analytics/v3.0/entities/recognition/general"

documents = {"documents": [
    {"id": "1", "text": "Microsoft is an It company."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(entities_url, headers=headers, json=documents)
entities = response.json()
pprint(entities)
