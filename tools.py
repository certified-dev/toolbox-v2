import random
import urllib.request
from urllib import request


def array_collector():
    gen_ticket_no = []
    while True:
        try:
            total_ticket = int(input('\nEnter Total Number of Booked Numbers:=>'))
            break
        except ValueError:
            print('             WARNING:enter a valid number!!!'
                  '\n'
                  '\n'
                  '\n'
                  )
    n = 1
    while n <= total_ticket:
        numbers = random.randrange(1, 99)
        if numbers in gen_ticket_no:
            continue
        gen_ticket_no.append(numbers)
        n += 1
    print(gen_ticket_no)

    while True:
        while True:
            try:
                user_ticket_no = int(input("\nChoose Any Number From 1 to 99 =>"))
                if user_ticket_no in gen_ticket_no:
                    while True:
                        try:
                            print('Ticket No', user_ticket_no, 'Is Not Available\n')
                            print('Here Are The Available Numbers')
                            # list available ticket numbers
                            for x in range(1, 99):
                                if x in gen_ticket_no:
                                    continue
                                print(x)
                            break
                        except ValueError:
                            print('             WARNING:enter a valid number!!!\n')
                else:
                    gen_ticket_no.append(user_ticket_no)
                    print('You Have Selected Ticket No', user_ticket_no)
                break
            except ValueError:
                print('      WARNING:enter a valid number!!!\n')


def web_img_dwnlder(url):
    name = random.randrange(1, 100)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


def usd_to_naira(usd):
    cvr_rate = int(input('how much is 1 dollar today in naira:# '))
    amount = int(usd) * cvr_rate
    print('$', usd, ' = ', '#', amount)
    print('\n')
    print('\n')
    usd_to_naira(int(input('enter amount in dollar:$ ')))


def btc_to_naira(btc):
    dollar_price_in_naira = int(input('how much is 1 dollar today in naira:# '))
    dollar_price_of_one_btc = int(input('how much is 1 btc today in dollar:$ '))
    amount = int(btc) * dollar_price_of_one_btc * dollar_price_in_naira
    print(btc, 'btc', ' = ', '#', amount)
    print('\n')
    print('\n')
    btc_to_naira(input('enter bitcoin amount: '))


def txt_grabber(txt_url):
    response = request.urlopen(txt_url)
    txt = response.read
    txt_str = str(txt)
    lines = txt_str.split("\\n")
    saved_txt = r'text.txt'
    fw = open(saved_txt, 'w')
    for line in lines:
        fw.write(line + '\n')
        fw.close()
