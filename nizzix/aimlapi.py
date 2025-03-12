import requests
import json

def talk_ai(prompt, history, aimlapi_keys, model="gpt-4o"):
    if not aimlapi_keys or aimlapi_keys == "[]" or aimlapi_keys == "":
        aimlapi_keys = [   # free key by nizzix
            "02ddf7e4b542411bb642d9528cb4c21c",   # free key by nizzix
            "fefbafc671d94e10bf1442c24ac7bbab",   # free key by nizzix
            "db1d188f233d42e98b71ce58c209d4b6",   # free key by nizzix
            "fa9f2ca20ed948aa911ae799c506d565",   # free key by nizzix
            "f62cad8c81d541ebab8c061c4754822b",   # free key by nizzix
            "41e4964442e24a47880978933ed5a8db",   # free key by nizzix
            "0b2cd1f9ccdb4817804de0183235930d",   # free key by nizzix
            "3bf8f6cbfa3b44d3ad7177b05859e8d3",   # free key by nizzix
            "d9b2eaeaf51046f192f5d55a65ac6ceb",   # free key by nizzix
            "e303e1f7157f4c3ba2a6ff34f2259c6e",   # free key by nizzix
            "ac1cadf93aba4470b253651c3d22af60"    # free key by nizzix
        ]   # free key by nizzix

    if not prompt:
        return {"error": "Prompt is required"}, 400
    
    if history != "" or history !="[]" or history != None:
        prompt = f"history: {history} prompt: " + prompt
        
    for api_key in aimlapi_keys:
        try:
            response = requests.post(
                url="https://api.aimlapi.com/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 512,
                    "stream": False,
                })
            )

            response.raise_for_status()

            # Parse et retourne la réponse
            result = response.json()
            readable_response = json.dumps(
                {"response": result['choices'][0]['message']['content']},
                ensure_ascii=False  
            )
            return json.loads(readable_response)

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429: 
                continue 
            return {"error": f"HTTP error occurred: {response.status_code} - {response.text}"}, response.status_code
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}, 500

    return {"error": "All API keys failed, please try again later or create your own key(s)"}, 500