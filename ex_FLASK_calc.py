from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def kalkulator():
    if request.method == "POST":
        liczba_1 = int(request.form["liczba_1"])
        liczba_2 = int(request.form["liczba_2"])
        dzialanie = request.form["dzialanie"]
        if dzialanie == "1":
            return '{} + {} = {}'.format(liczba_1, liczba_2, (liczba_1 + liczba_2))
        elif dzialanie == "2":
            return '{} - {} = {}'.format(liczba_1, liczba_2, (liczba_1 - liczba_2))
        elif dzialanie == "3":
            return '{} * {} = {}'.format(liczba_1, liczba_2, (liczba_1 * liczba_2))
        elif dzialanie == "4":
            return '{} / {} = {}'.format(liczba_1, liczba_2, (liczba_1 / liczba_2))
    else:
        return """
        <form action="/" method="POST">
            <label>Liczba 1:
                <input type="number" name="liczba_1">
            </label>
            <label>Liczba 2:
                <input type="number" name="liczba_2">
            </label>
            <label>Działanie do wykonania
                <select name="dzialanie">
                    <option value="1">dodaj</option>
                    <option value="2">odejmij</option>
                    <option value="3">pomnóż</option>
                    <option value="4">podziel</option>
                </select>
            </label>
            <label>
            <input type="submit" value="Podaj wynik"></input >
            </label>
        </form>
        """

app.run(debug=True)