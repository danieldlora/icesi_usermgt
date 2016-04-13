from flask import Flask
import commands
import json
app = Flask(__name__)

@app.route("/")
def hello():
    r= commands.getoutput('ls /home |sort')
    b=r.split("\n")
    users_di= {}
    users_di["users"]=b
    return  json.dumps(users_di)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

