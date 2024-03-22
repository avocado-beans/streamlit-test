import requests
url = "https://api.ai21.com/studio/v1/j2-mid/complete"

payload = {
    "prompt": "I don't think she likes me because",
    "numResults": 1,
    "maxTokens": 100,
    "minTokens": 0,
    "temperature": 0.7,
    "topP": 1,
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

start = 'completions":[{"data":{"text":'
end = '","tokens":[{"generatedToken"'
s = response.text
print(s[s.find(start)+len(start):s.rfind(end)])
