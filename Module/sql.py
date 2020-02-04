import mysql.connector

class db:

    def __init__(self, hostName, userName, password, db):

        try:
            self.conn = mysql.connector.connect(
            host=hostName,
            user=userName,
            passwd=password,
            database=db
            )
            if self.conn.is_connected():
                print("Connected")   

        except mysql.connector.Error as err:
            print(err)
            if err.errno == 1049: #Unknown database
                self.connect_db(hostName, userName, password)
                try:
                    self.query("CREATE DATABASE " + db)
                except mysql.connector.Error as err:
                    print(err)

    def connect_db(self, hostName, userName, password):
        try:
            self.conn = mysql.connector.connect(
            host=hostName,
            user=userName,
            passwd=password
            )
            if self.conn.is_connected():
                print("Connected")

        except mysql.connector.Error as err:
            print(err)

    def query(self, query):
        
        cursor = self.conn.cursor()

        try:
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err)
            if err.errno == 1146: #Table doesn't exist
                print('no table')
            return err

        self.conn.commit()
        cursor.close()

    def fetch(self, query, all: bool):
        cursor = self.conn.cursor(buffered=True)

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err)
            exit()

        if not all:
            return cursor.fetchone()
        
        return cursor.fetchall()

    def insertTo(self, table, column, value):
        q = "INSERT INTO " + table + " (" + column + ")" + " VALUES(" + value + ")"
        return self.query(q)

    def select(self, column, table, all: bool, order = None, limit = None, offset = None):
        q = "SELECT " + column + " FROM " + table

        if order is not None:
            q = q + " ORDER BY " + order

        if limit is not None:
            q = q + " LIMIT " + limit

        if offset is not None:
            q = q + " OFFSET " + offset

        return self.fetch(q, all)

    def selectAll(self, table, all: bool, order = None, limit = None, offset = None):
        q = "SELECT * " + "FROM " + table

        if order is not None:
            q = q + " ORDER BY " + order

        if limit is not None:
            q = q + " LIMIT " + limit

        if offset is not None:
            q = q + " OFFSET " + offset

        return self.fetch(q, all)

    def find(self, column, table, col, val, all: bool, order = None):
        q = "SELECT " + column + " FROM " + table + " WHERE " + col + " LIKE \"%" + val + "%\""

        if order is not None:
            q = q + " ORDER BY " + order

        return self.fetch(q, all)

    def findAll(self, table, key, all: bool, order = None):
        q = "SELECT * " + "FROM " + table + " WHERE " + key

        if order is not None:
            q = q + " ORDER BY " + order

        return self.fetch(q, all)

    def findCol(self, col, table, key, all: bool, order = None):
        q = "SELECT " + col + " FROM " + table + " WHERE " + key

        if order is not None:
            q = q + " ORDER BY " + order

        return self.fetch(q, all)

    def update(self, table, setValue, key):
        q = "UPDATE " + table + " SET " + setValue + " WHERE " + key
        return self.query(q)

    def delete(self, table, key = None):
        q = "DELETE FROM " + table

        if key is not None:
            q = q + " WHERE " + key

        return self.query(q)
