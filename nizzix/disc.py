import webbrowser
import time
import base64
import os 
import requests

class tool_discord():
    import webbrowser
    import time
    import base64
    import os 
    import requests
    '''Have a lot of tool for discord'''
    def id_to_token(userid):
        '''Transform an ID discord to an Start token'''
        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        print(f'FIRST PART : {encodedStr}')
        os.system('pause >nul') 

    def spam(msg, webhook_url):
        '''Spam an WebHook discord with the WebHook URL'''
        for i in range(30):
            try:   
                data = requests.post(webhook_url, json={'content': msg})
                if data.status_code == 204:           
                    print(f"Sent MSG {msg}")
            except:
                print("Bad Webhook :" + webhook_url)
                time.sleep(5)
                exit()

    def login_token(token):
        '''Login you with a token discord'''
        url = f"https://discord.com/login?token={token}"
        webbrowser.open(url)

    def check_token(token):
        '''Check a token Discord'''
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Authorization": token
        }
        
        try:
            response = requests.get("https://discord.com/api/v9/users/@me/library", headers=headers)
            if response.status_code == 200:
                valid_tokens.append(token)
                print(f"the token [{token}] is valid")
            elif response.status_code == 401:
                invalid_tokens.append(token)
                print("the token [{token}] is invalid")
        except Exception as e:
            print(f"error with [{token}]")

        valid_tokens = []
        invalid_tokens = []

class vp_discord():
    import webbrowser
    import time
    import base64
    import os 
    import requests
    '''for open VP_service discord'''
    def open_vpdicord():
        '''Open the discord VP link'''
        pastebin_url = 'https://raw.githubusercontent.com/hackiyui/discord/main/dicord'
        response = requests.get(pastebin_url)
        link = response.text
        webbrowser.open(link)