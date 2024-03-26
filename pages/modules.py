import requests
import json
from pprint import pprint

API_KEY = "2b10reEl4ESP60OUh0FhIcyu"  # Set you API_KEY here
PROJECT = "all" # try "weurope" or "canada"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
url = "https://api.ai21.com/studio/v1/j2-mid/complete"

def askAI21(prompt):
    payload = {
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 50,
        "minTokens": 0,
        "temperature": 0.,
        "topP": 0.,
        "topKReturn": 0,
        "frequencyPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "presencePenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "countPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer ZdMRvxwl0c1qvYrLa3fqveSVyLQdjPzv"
    }

    response = requests.post(url, json=payload, headers=headers)

    start = 'completions":[{"data":{"text":"'
    end = '","tokens":[{"generatedToken"'
    s = response.text
    finresult = s[s.find(start)+len(start):s.rfind(end)]
    finresult = finresult[2:] 
    return(finresult)

def getPlant(img_path):
    img_data = open(img_path, 'rb')

    data = {
        'organs': ['auto']
    }

    files = [
        ('images', (img_path, img_data))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    return json_result['results'][0]['species']['scientificNameWithoutAuthor'], json_result['results'][0]['species']['commonNames'][0] 
    
