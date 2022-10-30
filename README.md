# discauth
##setup

*installation*
```pip install discauth```

##basic usage
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
  token = code_to_token(client_id, client_secret, redirect, code)
  session['token'] = str(token)
  return redirect('http://localhost:5000')
 
 @app.route('/logout')
 def logout():
  session.clear()
  return redirect('/')```
  
