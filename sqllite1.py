import sqlite3 as lite

con = lite.connect('./db/sqlite_db1.db')


res = con.execute("select * from USERS")

user_dic = dict()

for user in res:
    user_dic['name'] = user[0]
    user_dic['email'] = user[1]

print user_dic    
