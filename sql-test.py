import sqlite3

con = sqlite3.connect("/home/yuto/ドキュメント/sqlite-test.db")
cur = con.cursor()

cur.execute("""
    delete from member where id = 3;
""")

con.commit()
con.close()
