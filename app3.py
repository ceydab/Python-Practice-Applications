
account1 = {
    'name' : 'Cyrile',
    'accountno' : '1234',
    'money' : 300,
    'addacc' : 200
}
account2 = {
    'name' : 'Cyrus',
    'accountno' : '5678',
    'money' : 400,
    'addacc' : 100
}

def getMoney(account, amount):
    print(f"Hello {account['name']}")
    if account['money'] >= amount:
        print('You can have your money.')
        account['money'] -= amount
    else:
        sum = account['money'] + account['addacc']
        if sum >= amount:
            print('Not enough money.')
            print(f"{account['accountno']} account has {account['money']}, additional account has {account['addacc']}")

            answer = input('Would you like to use the additional account? (y/n) \n')
            if answer == 'y':
                print('You can have your money')
                howmuch = amount - account['money']
                account['money'] = 0
                account['addacc'] -= howmuch
                print(f"{account['accountno']} account has {account['money']}, additional account has {account['addacc']}")
            else: 
                print(f"{account['accountno']} account has {account['money']}, additional account has {account['addacc']}")
        else:
            print('Not enough money.')
            print(f"{account['accountno']} account has {account['money']}, additional account has {account['addacc']}")

getMoney(account2, int(input('amount: ')))