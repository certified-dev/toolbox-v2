import os
import sqlite3
from user import *
from main import *

if os.path.exists('db.sqlite'):
    print('\n')
    try:
        sqliteConnection = sqlite3.connect('db.sqlite')
        cursor = sqliteConnection.cursor()
        var_login = [os.getlogin()]
        cursor.execute("SELECT Username FROM Users Where Id = ?", var_login)
        record = cursor.fetchone()
        username = record[0]
        cursor.close()
        sqliteConnection.close()
        user_id = [username]
        print('[*] Username:', username)
        try:
            password = input('[*] Password: ')
            with sqlite3.connect('db.sqlite') as db:
                cursor = db.cursor()
                cursor.execute("SELECT Password FROM Users WHERE Username = ?", user_id)
                result = cursor.fetchone()
                password1 = result[0]
                if password == password1:
                    session()
                else:
                    print('    Wrong password!!!\n')
                    incorrect_pwd()
        except sqlite3.Error as error:
            print(error)
            print('                          You Are Not A Registered User!!! ')
            print('           Enter Your details Correctly to Signup And Continue Using This Product\n')
    except sqlite3.Error as error:
        print('                            You Are Not A Registered User!!! ')
        print('           Enter Your details Correctly to Signup And Continue Using This Product\n')
        print('\n')
        register()
    finally:
        pass
else:
    print('                                                                               ')
    print('                                 SIGN UP NOW!!! ')
    print('          Please Enter Your details Correctly to Continue Using This Product \n')
    print('\n')
    register()
