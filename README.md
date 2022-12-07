# discauth
**setup**

*installation*
`git clone "https://github.com/uiisback/discauth`
||make sure this is in the same folder as your code you want to write but make
sure discauth is a separate folder||
**Basic usage**

*flask login system returns username*

```py
from discauth import *
import flask
from flask import *
config = {
  "client_secret" : "YOUR_CLIENT_SECRET",
  "client_id" : "YOUR CLIENT_ID",
  "OAUTH_URI" : "OAUTH_URL",
  "redirect" : "YOUR_REDIRECT"
 }
  
app = Flask(__name__)
@app.route('/login')
def login():
  if 'token' in session:
    user_data = get_user_data(session['token'])
    username = user_data['username'] + "#" + user_data['discriminator']
    return "logged in as {username} <a href="/logout"><button>logout</a></button>
  return f"""
  
  <a href={OAUTH_URI}><button>login with discord</button></a>
  
  """

@app.route('/callback')
def callback():
  code = request.args.get('code')
  token = code_to_token(config['client_id'], config['client_secret'], config['redirect'], config['code'])
  session['token'] = str(token)
  return redirect('/')
 
 @app.route('/logout')
 def logout():
  session.clear()
  return redirect('/')
  ```
  
*Dragging a user to a guild*
```py
from discauth import *
config = {
  "bearer_token" : "YOUR_BEARER_TOKEN", #this is the token you get from the code_to_token function
  "bot_token" : "YOUR_BOT_TOKEN", #the bot must be in the guild you're dragging to
  "user_id" : "USER_TO_DRAG_ID",
  "guild_id" : "GUILD_ID_TO_DRAG_TO"
} 
pull = pull_to_guild(bot_token, bearer_token, guild_id, user_id)
print(pull)
```





  
