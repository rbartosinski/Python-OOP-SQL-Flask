from flask import Flask
from flask import request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def code():
    if request.method == "POST":
        n = request.form["code"]
        return matching(n)
    else:
        return form

form = """
        <form action="/" method="POST">
            <label>Twój kod pocztowy:
                <input type="text" name="code">
            </label>
            <label>
                <input type="submit" value="Sprawdź"></input >
            </label>
        </form>
        """
import re

def matching(arg):
    if len(arg) == 6:
        wzor = (r'\d\d-\d\d\d')
        r = re.compile(wzor)
        if r.match(arg):
            return "Kod poprawny"
        else:
            return "Kod niepoprawny"
    else:
        return "Kod niepoprawny"

app.run(debug=True)