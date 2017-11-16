from mysql.connector import connect

class DBconnection:

    def __init__(self, user, password, database, host="127.0.0.1"):
        self.cnx = connect(user=user, password=password,
                  host=host, database=database)
        self.cursor = self.cnx.cursor()

    def insert(self, table, data_dict):
        columns = []
        values = []
        for key, val in data_dict.items():
            columns.append(key)
            values.append("'%s'" % val)

        sql = """INSERT INTO {}({})
        VALUES ({});
        """.format(table, ', '.join(columns), ', '.join(values))
        self.cursor.execute(sql)
        self.cnx.commit()
        return self.cursor.lastrowid

    def select(self, table, column='', value=''):
        sql = "SELECT * FROM {}".format(table)
        if column:
            sql += " WHERE {}='{}'".format(column, value)
        self.cursor.execute(sql)
        results = []
        for record in self.cursor:
            results.append(record)
        return results

    def select_adv(self, table, column, operation, value):
        sql = "SELECT * FROM {} WHERE {} {} '{}'".format(table, column, operation, value)
        self.cursor.execute(sql)
        results = []
        for record in self.cursor:
            results.append(record)
        return results

    def select_between(self, table, column, value_a, value_b):
        sql = "SELECT * FROM {} WHERE {} BETWEEN '{}' AND '{}'".format(table, column, value_a, value_b)
        self.cursor.execute(sql)
        results = []
        for record in self.cursor:
            results.append(record)
        return results

    def delete(self, table, column, value):
        sql = "DELETE FROM {} WHERE {}='{}'".format(table, column, value)
        self.cursor.execute(sql)
        self.cnx.commit()
        return self.cursor.lastrowid