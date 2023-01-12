import sqlite as sql
from datetime import datetime
from formatting import color


class Library:
    def __init__(self, name, db):
        self.name = name
        self.con = sql.connection(db)
        if sql.create_new(self.con):
            print(color["success"], "Created.\n", color["success"], "Database Connected.")
        else:
            print(color["success"], "Database Connected.")

    def add_user(self, username, phone, name, family, birthday, nclass, fname, school, email=False):
        """Create user in database for using in library"""

        date = datetime.today().strftime('%Y-%m-%d')
        cursor = self.con.cursor()
        if email:
            entities = (username, phone, email, name, family, birthday, nclass, fname, date, school)
            cursor.execute("INSERT INTO users(username, phone, email, name, family, birthday, class, fname, date,\
             school) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", entities)
        else:
            entities = (username, phone, name, family, birthday, nclass, fname, date, school)
            cursor.execute("INSERT INTO users(username, phone, name, family, birthday, class, fname, date, school)\
             VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", entities)
        self.con.commit()

    def edit_user(self, uid, table, value, vtype="str"):
        """Edit created user in database with id and table"""

        cursor = self.con.cursor()
        if vtype == "str":
            execute = "UPDATE users SET " + str(table) + " = '" + str(value) + "' where id = " + str(uid)
        else:
            execute = "UPDATE users SET " + str(table) + " = " + str(value) + " where id = " + str(uid)
        cursor.execute(execute)
        self.con.commit()

    def get_user_value(self, uid, table):
        """Get user custom value with id"""

        cursor = self.con.cursor()
        cursor.execute("SELECT " + str(table) + " FROM users where id = " + str(uid))
        value = cursor.fetchall()[0][0]

        return value

    def get_user_id(self, username):
        """Get user by username return user id"""

        cursor = self.con.cursor()
        cursor.execute("SELECT id FROM users where username = '" + str(username) + "'")
        uid = cursor.fetchall()[0][0]

        return int(uid)
