import sqlite3 as lite
import urllib2
import bs4

con = lite.connect('./db/new_db.db')

v_stm = '''CREATE TABLE IF NOT EXISTS PAGES
         ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, URL TEXT,
           HTML TEXT UNIQUE)'''

con.execute(v_stm)

v_stm = '''INSERT OR IGNORE INTO PAGES (URL,HTML) VALUES ('wwww.test.com','index.html')'''

con.execute(v_stm)

con.commit()
con.close()
