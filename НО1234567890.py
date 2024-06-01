import requests
from keys import key, id


def gpt(text):
    prompt = {
        "modelUri": f"gpt://{id}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role":"assisttent",
                "text":text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {key}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    print(response)
    result = response.json().get('result')
    print(result)
    return result['alternatives'][0]['message']['text']


print(gpt('как отчистить природу от загризнений '))