from flask import Flask
from flask import request
from flask import render_template
from dbconnection import DBconnection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def all_form_day_one():
    if request.method == "GET":
        return render_template("index.html")

    else:
        db = DBconnection(user="root", password="cnxpass", database="cinemas_db")
        if request.form["submit"] == "add_cinema":
            new_cinema = {"name": request.form["name"],
                          "address": request.form["address"]}
            db.insert("Cinema", new_cinema)
            return "Zapisano kino w bazie danych." + render_template("index.html")

        elif request.form["submit"] == "remove_cinema":
            cinema_to_remove = request.form["name"]
            db.delete("Cinema", "name", cinema_to_remove)
            return "Usunięto kino z bazy danych." + render_template("index.html")

        elif request.form["submit"] == "show_cinemas":
            Cinemas = db.select("Cinema")
            return "<h2>Lista wszystkich kin:</h2>" + str(Cinemas) + render_template("index.html")

        elif request.form["submit"] == "search_cinema":
            cinema_to_search = request.form["name"]
            searched_cin = db.select("Cinema", "name", cinema_to_search)
            return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: {}</h2>".format(
                cinema_to_search) + str(searched_cin) + render_template("index.html")

        elif request.form["submit"] == "add_movie":
            if 0 < float(request.form["rating"]) < 10:
                new_movie = {"name": request.form["name"],
                              "description": request.form["desc"],
                              "rating": request.form["rating"]}
                db.insert("Movie", new_movie)
                return "Zapisano film w bazie danych." + render_template("index.html")
            else:
                return "Ocena filmu musi mieścić się w 10!" + render_template("index.html")

        elif request.form["submit"] == "remove_movie":
            movie_to_remove = request.form["name"]
            db.delete("Movie", "name", movie_to_remove)
            return "Usunięto film z bazy danych." + render_template("index.html")

        elif request.form["submit"] == "show_movies":
            Movies = db.select("Movie")
            return "<h2>Lista wszystkich filmów:</h2>" + str(Movies) + render_template("index.html")

        elif request.form["submit"] == "search_mov_by_name":
            movie_to_search = request.form["name"]
            searched_mov_by_name = db.select("Movie", "name", movie_to_search)
            return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: {}</h2>".format(
                movie_to_search) + str(searched_mov_by_name) + render_template("index.html")

        elif request.form["submit"] == "search_mov_by_rate":
            movie_to_search = request.form["rating"]
            searched_mov_by_rate = db.select("Movie", "rating", movie_to_search)
            return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: Rating: {}</h2>".format(
                movie_to_search) + str(searched_mov_by_rate) + render_template("index.html")

        elif request.form["submit"] == "add_ticket":
            if float(request.form["price"]) > 0:
                new_ticket = {"quantity": request.form["quantity"],
                              "price": request.form["price"]}
                db.insert("Ticket", new_ticket)
                return "Zapisano bilet w bazie danych." + render_template("index.html")
            else:
                return "Cena biletu musi być wieksza od zera" + render_template("index.html")

        elif request.form["submit"] == "remove_ticket":
            ticket_to_remove = request.form["ID"]
            db.delete("Ticket", "id", ticket_to_remove)
            return "Usunięto bilet z bazy danych." + render_template("index.html")

        elif request.form["submit"] == "add_payment":
            new_payment = {"type": request.form["payment_type"],
                          "data": request.form["payment_date"]}
            db.insert("Payment", new_payment)
            return "Zapisano płatność w bazie danych." + render_template("index.html")

        elif request.form["submit"] == "remove_payment":
            ticket_to_remove = request.form["ID"]
            db.delete("Payment", "id", ticket_to_remove)
            return "Usunięto płatność z bazy danych." + render_template("index.html")

        elif request.form["submit"] == "show_payments":
            Payments = db.select("Payment")
            return "<h2>Lista wszystkich płatności:</h2>" + str(Payments) + render_template("index.html")

        elif request.form["submit"] == "search_payment":
            if request.form["payment_search_type"] == "day":
                payment_to_search = request.form["payment_date_from"]
                searched_payment = db.select("Payment", "data", payment_to_search)
                return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: Wg dnia: {}</h2>".format(
                    payment_to_search) + str(searched_payment) + render_template("index.html")

            elif request.form["payment_search_type"] == "older":
                payment_to_search = request.form["payment_date_from"]
                searched_payment = db.select_adv("Payment", "data", "<", payment_to_search)
                return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: Starsze niż: {}</h2>".format(
                    payment_to_search) + str(searched_payment) + render_template("index.html")

            elif request.form["payment_search_type"] == "newer":
                payment_to_search = request.form["payment_date_from"]
                searched_payment = db.select_adv("Payment", "data", ">", payment_to_search)
                return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: Nowsze niż: {}</h2>".format(
                    payment_to_search) + str(searched_payment) + render_template("index.html")

            elif request.form["payment_search_type"] == "between":
                payment_to_search_a = request.form["payment_date_from"]
                payment_to_search_b = request.form["payment_date_to"]
                searched_payment = db.select_between("Payment", "data", payment_to_search_a, payment_to_search_b)
                return "<h2>Wyszukiwanie zakończone. Wyświetlam wyniki zapytania dla: Zakres: {} - {}</h2>".format(
                    payment_to_search_a, payment_to_search_b) + str(searched_payment) + render_template("index.html")

app.run(debug=True)
