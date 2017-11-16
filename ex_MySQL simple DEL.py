#DELETE FROM Product WHERE id=5;

from flask import Flask
from flask import request
from mysql.connector import connect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show():
    product_id = request.args.get("id")
    if product_id is not None:
        cnx = connect(user="root", password="coderslab",
                      host="127.0.0.1", database="exercises_db")
        cursor = cnx.cursor()

        sql = "DELETE FROM Product WHERE id=%s" % product_id
        cursor.execute(sql)
        cnx.commit()
        aff = cursor.rowcount

        cursor.close()
        cnx.close()

        return "Ok. Deleted %s product(s)" % aff

    return "Wprowadź id produktu"

app.run(debug=True)