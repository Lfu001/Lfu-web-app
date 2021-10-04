import sqlite3
import os


def addHistory(shape, data):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "history.sqlite3"))
    cur = con.cursor()

    if shape == "rectangle":
        cur.execute("insert into rectHistory values(" + ", ".join([str(d) for d in data]) + ");")

    if shape == "circle":
        cur.execute("insert into circHistory values(" + ", ".join([str(d) for d in data]) + ");")

    con.commit()
    con.close()


def getHistory(shape):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "history.sqlite3"))
    cur = con.cursor()

    if shape == "rectangle":
        cur.execute("select * from rectHistory;")

    if shape == "circle":
        cur.execute("select * from circHistory;")

    return cur.fetchall()
