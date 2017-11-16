from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def post_get():
    if request.method == "POST":
        return "Wysłałeś POST"
    else:
        return "Wysłałeś GET"

# do testu w terminalu: curl --request POST http://localhost:5000/

app.run(debug=True)