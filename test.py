import requests
import json
API_KEY = '<your api key here bud'
#the url keeps changing so visit the official docs of openai for the latest url
#also rememeber to encrypt your key before uploading to git
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {
    'Content-Type': 'application/json'
}
while True:
    user_input = input("Enter your query (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the program...")
        break

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }


    response = requests.post(url, headers=headers, data=json.dumps(payload))


    if response.status_code == 200:

        response_data = response.json()
        message = response_data['candidates'][0]['content']['parts'][0]['text']
        print("Response:", message)
    
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
