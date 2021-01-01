import random
import sys

class Account:
    def __init__(self, card_num=None, pin=None):
        self.card_num = card_num
        self.pin = pin
        self.balance = 0

    def generate_card_num(self):
        iin = '400000'
        acc_id = random.randint(0, 999999999)
        acc_id = str(acc_id).zfill(9)
        checksum = str(random.randint(0, 10))
        self.card_num = int(iin + acc_id + checksum)
        return self.card_num

    def generate_pin(self):
        pin = random.randint(0, 9999)
        pin = str(pin).zfill(4)
        self.pin = pin
        return self.pin


def main_menu():
    print('''1. Create an account
2. Log into account
0. Exit''')
    menu_selection = input()
    if menu_selection == '1':
        new_account = Account()
        card_num = new_account.generate_card_num()
        pin = new_account.generate_pin()
        account = {card_num: pin}
        balance = {card_num: '0'}
        accounts.update(account)
        balances.update(balance)
        print(f'''Your card has been created
Your card number:
{card_num}
Your card pin:
{pin}
''')
        print(accounts)
        print('')
        return card_num
    elif menu_selection == '2':
        card_num = input('Enter your card number:')
        pin = input('Enter your pin:')
        log_in(card_num, pin)
        print('')
        menu_2_selection = menu_2(card_num)
        return menu_2_selection
    else:
        print('Bye!')
        sys.exit()


def menu_2(card_num):
    print(('''1. Balance
2. Log out
0. Exit
'''))
    menu_2_selection = input()
    if menu_2_selection == '1':
        check_balance(card_num)
        print('')
        menu_2_selection = menu_2(card_num)
    elif menu_2_selection == '2':
        print('''You have successfully logged out!
        ''')
        menu_selection = main_menu()
        return menu_selection
    else:
        print('Bye!')
        sys.exit()
    return menu_2_selection

def log_in(card_num, pin):
    if int(card_num) in accounts and pin == accounts[int(card_num)]:
            print('You have successfully logged in!')
    else:
        print('''Wrong card or PIN!
        ''')
        menu_selection = main_menu()
        return menu_selection

def check_balance(card_num):
    print('Balance:' + balances[int(card_num)])



accounts = {}
balances = {}
menu_selection = main_menu()
while menu_selection != '0':
    menu_selection = main_menu()
