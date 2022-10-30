import requests
API_ENDPOINT = "https://discord.com/api/v8"
def code_to_token(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, code):
    data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
    }
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers)
    if "invalid".lower() in r.json():
        return "[error] it seems one of your values are incorrect please double check!"
    else:
        return r.json()['access_token']
def get_user_data(token):
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    r = requests.get(API_ENDPOINT, headers = headers)
    return r.json()
def pull_to_guild(bot_token, token, guild_id, id):
    
    data = {
        "access_token" : token
    }
    headers = {
        "Authorization" : f"Bot {bot_token}",
        'Content-Type': 'application/json'

    }
    r = requests.put(f'{API_ENDPOINT}/guilds/{guild_id}/members/{id}', headers=headers, json=data).json()
    return r
def view_guilds(token):
    url = API_ENDPOINT + "/users/@me/guilds"
    headers = {
               "Authorization" : f"Bearer {token}" 
    }
    r = requests.get(url, headers=headers)
    return r.json()
def view_connections(token):
    url = API_ENDPOINT + "/users/@me/connections"
    headers = {
               "Authorization" : f"Bearer {token}" 
    }
    r = requests.get(url, headers=headers)
    return r.json()
