import sqlite3
import hashlib
import os
import datetime

import base64



users = sqlite3.connect('data/users.db')
users_cur = users.cursor()

works = sqlite3.connect('data/works.db')
works_cur = works.cursor()


def create_db():
    users_cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INTEGER PRIMARY KEY AUTOINCREMENT,
       login TEXT NOT NULL,
       password TEXT NOT NULL);
    """)
    users.commit()

    works_cur.execute("""CREATE TABLE IF NOT EXISTS works(
           workid INTEGER PRIMARY KEY AUTOINCREMENT,
           theme TEXT NOT NULL,
           varcount INTEGER NOT NULL,
           excount INTEGER NOT NULL,
           fileformat TEXT NOT NULL,
           userid INTEGER NOT NULL,
           creation_date TEXT NOT NULL);
        """)
    works.commit()


def add_new_user(new_login, new_password):
    s = base64.b64encode(new_password).decode('utf-8')
    users_cur.execute(f"INSERT INTO users (login, password) VALUES ('{new_login}', '{s}');")
    users.commit()


def add_new_work(theme, varcount, excount, fileformat, userid):
    works_cur.execute(f"INSERT INTO works (theme, varcount, excount, fileformat, userid, creation_date) \
    VALUES ('{theme}', '{varcount}', '{excount}', '{fileformat}', '{userid}', '{datetime.date.today()}');")
    works.commit()


def get_all_users_works(userid):
    works_cur.execute(f"SELECT * FROM works;")
    works_list = works_cur.fetchall()
    return [work for work in works_list if work[4] == userid]


def check_user(login):
    print(login)
    users_cur.execute(f"SELECT * FROM users;")
    users_list = users_cur.fetchall()
    print(users_list)
    return any([login in elem for elem in users_list])


def get_user(login):
    print(login)
    users_cur.execute(f"SELECT * FROM users;")
    users_list = users_cur.fetchall()
    print('ok')
    return [elem for elem in users_list if elem[1] == login]


def hashUsersPassword(password, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000,
        dklen=128
    )
    return salt + key


def check_password(db_password, input_password):
    salt = base64.b64decode(db_password.encode("utf-8"))[:32]
    print(db_password == str(base64.b64encode(hashUsersPassword(input_password, salt)), "utf-8"), sep="\n")
    return db_password == str(base64.b64encode(hashUsersPassword(input_password, salt)), "utf-8")
