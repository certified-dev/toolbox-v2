import time
import sqlite3
from tools import *
import os
import datetime

from tools import txt_grabber


def session():
    time.sleep(1)
    print('\n')
    check_birthday()
    log_time = time.ctime()
    print('''

                                            ''')
    print('     --------------------User logged in @ : ' + str(log_time) + '--------------------\n')
    choice = int(input('''                              ____________[*] AVAILABLE TOOLS [*]_____________

                                          [1] Text Grabber

                                          [2] Web Image Scrapper 

                                          [3] Currency To Naira Converter 

                                          [4] Ticket Reservation 

                                          [*] Enter 0 to Edit Your Details 

                    
                  => '''))
    if choice == 1:
        txt_grabber(input('''
    Enter text full url path:
     => '''))
    elif choice == 2:
        web_img_dwnlder(str('https://') + input('''
     Enter web address:
     => '''))
    elif choice == 3:
        btc_choice = int(input('''
                                       [1] US Dollar To Naira 

                                       [2] Bitcoin Core to Naira 
    => '''))
        if btc_choice == 1:
            usd_to_naira(int(input('enter amount in dollar:$ ')))
        elif btc_choice == 2:
            btc_to_naira(input('enter bitcoin amount: '))
    elif choice == 4:
        array_collector()
    elif choice == 0:
        edit = input('''            What would you like to edit?
        
                         [1] Occupation
                         [2] Phone Number
                         [3] Password
            =>: ''')
        with sqlite3.connect('db.sqlite') as db:
            if edit == '1':
                new_edit = input('Occupation: ')
                var_new_edit = [new_edit, os.getlogin()]
                cursor = db.cursor()
                cursor.execute("UPDATE Users SET Occupation = ? where Id = ?", var_new_edit)
                print('saved')
                db.commit()
                cursor.close()

            elif edit == '2':
                new_edit = input('Telephone: ')
                var_new_edit = [new_edit, os.getlogin()]
                cursor0 = db.cursor()
                cursor0.execute("UPDATE Users SET Phone = ? where Id = ?", var_new_edit)
                print('saved')
                db.commit()
                cursor0.close()

            elif edit == '3':
                var_login = [os.getlogin()]
                cursor1 = db.cursor()
                cursor1.execute("SELECT Username FROM Users Where Id = ?", var_login)
                record = cursor1.fetchone()
                username = record[0]
                user_id = [username]
                cursor1.close()

                old_pwd = input('Current password: ')
                cursor2 = db.cursor()
                cursor2.execute("SELECT Password FROM Users WHERE Username = ?", user_id)
                result = cursor2.fetchone()
                db_pwd = result[0]
                cursor2.close()

                if old_pwd == db_pwd:
                    new_pwd = input('New password: ')
                    check_new_pwd = input('Verify new password: ')
                    if new_pwd == check_new_pwd:

                        var_set_pwd = [check_new_pwd, username]
                        cursor3 = db.cursor()
                        cursor3.execute("UPDATE Users SET Password = ? WHERE Username = ?", var_set_pwd)
                        db.commit()
                        cursor3.close()
                        print('\nPassword Changed successfully!!!\n')
                        time.sleep(2)
                        session()
                    else:
                        print('Passwords does not match!!!')
                else:
                    print('Current password incorrect!!!')
            else:
                pass
    else:
        exit()


def check_birthday():
    with sqlite3.connect('db.sqlite') as db:
        cursor = db.cursor()
        var = [os.getlogin()]
        cursor.execute("SELECT Dob FROM Users Where Id = ?", var)
        record = cursor.fetchone()
        saved_dob = record[0]
        cursor.close()

        mm_dd = saved_dob[5:]
        cur_date = datetime.date.today()
        new_date = str(cur_date)
        if mm_dd in new_date:
            birth_year = saved_dob[:4]
            age = int(cur_date.year - int(birth_year))
            new_age = str(age)

            cursor1 = db.cursor()
            var2 = [os.getlogin()]
            cursor1.execute("SELECT Name FROM Users Where Id = ?", var2)
            read_name = cursor1.fetchone()
            referred = read_name[0]
            cursor1.close()

            if new_age[1:] is '1':
                print('\nHappy', str(age) + 'st', 'Birthday, Dear', referred, 'Wishing You Success\n')
                time.sleep(5)
            elif new_age[1:] is '2':
                print('\nHappy', str(age) + 'nd', 'Birthday, Dear', referred, 'Wishing You Success\n')
                time.sleep(5)
            elif new_age[1:] is '3':
                print('\nHappy', str(age) + 'rd', 'Birthday, Dear', referred, 'Wishing You Success\n')
                time.sleep(5)
            else:
                print('\nHappy', str(age) + 'th', 'Birthday, Dear', referred, 'Wishing You Success\n')
                time.sleep(5)
        else:
            pass
