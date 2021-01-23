import random
import sys

class Account:
    def __init__(self, card_num=None, pin=None):
        self.card_num = card_num
        self.pin = pin
        self.balance = 0

    def generate_card_num(self):
        def luhn(num):
            odd_digits = []
            even_digits = []
            all_digits = []
            total = 0
            for x in range(len(num)):
                if x % 2 == 0:
                    odd_digits.append(int(num[x]))
                else:
                    even_digits.append(int(num[x]))
            for x in range(len(odd_digits)):
                odd_digits[x] = odd_digits[x] * 2
            for x in range(len(odd_digits)):
                if odd_digits[x] > 9:
                    odd_digits[x] -= 9
            for x in odd_digits:
                all_digits.append(x)
            for x in even_digits:
                all_digits.append(x)
            for x in all_digits:
                total += x
            if total % 10 == 0:
                checksum = 0
                return checksum
            else:
                i = str(total)
                i = i[-1]
                i = int(i)
                checksum = 10 - i
                return checksum

        iin = '400000'
        acc_id = random.randint(0, 999999999)
        acc_id = str(acc_id).zfill(9)
        num = str(iin) + acc_id
        num = num + str(luhn(num))
        return num


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
    if card_num in accounts and pin == accounts[card_num]:
            print('You have successfully logged in!')
    else:
        print('''Wrong card or PIN!
        ''')
        menu_selection = main_menu()
        return menu_selection

def check_balance(card_num):
    print('Balance:' + balances[card_num])



accounts = {}
balances = {}

menu_selection = main_menu()

while menu_selection != '0':
    menu_selection = main_menu()
