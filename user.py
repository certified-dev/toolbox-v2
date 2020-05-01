from toolbox_v2.db import *
from toolbox_v2.main import *
import os
import sqlite3
import time
import sys


def register():
    global os_id
    if os.path.exists('db.sqlite'):
        pass
    else:
        init()
        def linux_test():
            assert ('linux' in sys.platform)
        try:
            linux_test()
        except AssertionError:
            print('windows detected')
            var = []
            new = sys.getwindowsversion()
            for x in new:
                var.append(x)
            a = str(var.pop())
            b = str(var.pop())
            c = str(var.pop())
            d = str(var.pop())
            e = str(var.pop())
            os_id = e + '.' + d + '.' + c + '.' + b + '.' + a
        else:
            pass
        collect(
            os.getlogin(),
            input('Full Name: '),
            input('Email: '),
            input('Birth Date (YYYY-MM-DD): '),
            input('Home Address: '),
            input('Occupation: '),
            input('Telephone: '),
            os_id
        )
        print('\n')
        time.sleep(2)
        username = str(input('Enter Preferred Username: '))
        # check if username is available
        sqliteConnection = sqlite3.connect('db.sqlite')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT username FROM Users")
        records = cursor.fetchall()
        record = str(records)
        cursor.close()
        sqliteConnection.close()
        if username in record:
            # -------------username is not available-------------------
            print('Username not available')
        else:
            # --------------username is available-----------------------
            pass

        def pwd():
            # -------------choose a password-----------------------------
            password = str(input('Choose a password: '))
            password1 = str(input('Please confirm password: '))
            # -------------check if both entries match-----------------------
            if password == password1:
                # -------------match-----------------------------
                # --------------send all entries to db---------------------
                with sqlite3.connect('db.sqlite') as db:
                    var_insert = [username, os.getlogin()]
                    cursor0 = db.cursor()
                    cursor0.execute("UPDATE Users SET Username = ?  WHERE Id = ? ", var_insert)
                    var_insert.pop(0)
                    var_insert.insert(0, password1)
                    cursor0.execute("UPDATE Users SET Password = ?  WHERE Id = ? ", var_insert)
                    db.commit()
                    cursor0.close()
                    print('\n')
                    print('\n')
                    print('\nRegistering User [20%]')
                    time.sleep(2)
            else:
                # -------------no match-----------------------
                print('Passwords does not match')
                pwd()

        pwd()
    print('''




               ''')
    print('\n          << User Account Created Successfully!!! >>>')
    print('\n')
    print('\n')
    session()


def incorrect_pwd():
    with sqlite3.connect('db.sqlite') as db:
        # -------------get username from db via win_name---------------------------
        login = [os.getlogin()]
        cursor = db.cursor()
        cursor.execute("SELECT Username FROM Users Where Id = ?", login)
        record = cursor.fetchone()
        username = record[0]
        user_id = [username]

        password = input('[*] Password: ')
        # ---------------fetch password from db via username---------------------------
        cursor.execute("SELECT Password FROM Users WHERE Username = ?", user_id)
        result = cursor.fetchone()
        password1 = result[0]
        cursor.close()
        if password == password1:
            session()
        else:
            print('    Wrong password!!!\n')
            password = input('[*] Password: ')
            cursor = db.cursor()
            # ---------------fetch password from db via username--------------------------
            cursor.execute("SELECT Password FROM Users WHERE Username = ?", user_id)
            result = cursor.fetchone()
            password2 = result[0]
            if password == password2:
                session()
            else:
                print('     Wrong password!!!\n')
                asked = input('Forgotten Password? (y/n): ')
                print('\n')
                if asked == 'y':
                    print('[*] contact us on toolbox_team@dev_org.com to retrieve password')
                    time.sleep(5)
                elif asked == 'n':
                    incorrect_pwd()
