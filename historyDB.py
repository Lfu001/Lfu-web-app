import sqlite3
import os


def addHistory(shape, data):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "history.sqlite3"))
    cur = con.cursor()

    values = ", ".join([str(d) if not isinstance(d, str) else "'" + d + "'" for d in data])

    if shape == "rectangle":
        cur.execute("insert into rectHistory values(" + values + ");")

    if shape == "circle":
        cur.execute("insert into circHistory values(" + values + ");")

    con.commit()
    con.close()


def getHistory(shape, user_id):
    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "history.sqlite3"))
    cur = con.cursor()

    if shape == "rectangle":
        cur.execute("select a, b, result, timestamp from rectHistory where user_id = '" + user_id + "' order by timestamp desc;")

    if shape == "circle":
        cur.execute("select r, result, timestamp from circHistory  where user_id = '" + user_id + "' order by timestamp desc;")

    return cur.fetchall()
