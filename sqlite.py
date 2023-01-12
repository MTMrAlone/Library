import sqlite3
from sqlite3 import Error, OperationalError
from os.path import exists


def connection(location):
    try:
        con = sqlite3.connect(location)
        return con
    except Error:
        print(Error)


def create_new(con):
    cursor = con.cursor()
    try:
        cursor.execute("""CREATE TABLE "books" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	"release"	TEXT NOT NULL,
	"author"	TEXT NOT NULL,
	"access"	INTEGER NOT NULL DEFAULT 1,
	"used"	INTEGER NOT NULL DEFAULT 0,
	"using"	INTEGER NOT NULL DEFAULT 0,
	"isbn"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT))""")
        cursor.execute("""CREATE TABLE "logs" (
	"id"	INTEGER NOT NULL,
	"type"	INTEGER NOT NULL DEFAULT 1,
	"date"	TEXT NOT NULL,
	"info"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT))""")
        cursor.execute("""CREATE TABLE "users" (
	"id"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	INTEGER NOT NULL DEFAULT 1111,
	"phone"	TEXT NOT NULL,
	"email"	TEXT,
	"name"	TEXT NOT NULL,
	"family"	TEXT NOT NULL,
	"birthday"	TEXT,
	"date"	TEXT NOT NULL,
	"class"	INTEGER NOT NULL,
	"school"	TEXT NOT NULL,
	"fname"	TEXT,
	"level"	INTEGER NOT NULL DEFAULT 1,
	"book"	INTEGER NOT NULL DEFAULT 0,
	"in"	INTEGER NOT NULL DEFAULT 0,
	"out"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT))""")
        cursor.execute("""CREATE TABLE "rents" (
	"id"	INTEGER NOT NULL,
	"uid"	INTEGER NOT NULL,
	"bid"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	"return"	INTEGER NOT NULL DEFAULT 7,
	"status"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT))""")
        con.commit()
    except OperationalError:
        return False
    else:
        return True
