import datetime


user={
    "name":"Arthur",
    "surname":"Morgan",
    "pin":4590,
    "balance":1000.0,  # USD
    "transactionHistory":"\n"
                         "Walmart-78.56$-----Date:[03-11-2023]-----Time:[23:13.03]\n"
                         "Binance-100$-----Date:[09-11-2023]-----Time:[03:25:10]\n"   
                         "Cashing out-500$-----Date:[19-11-2023]-----Time:[14:47:53]\n"
                         "Micro Center-2345$-----Date:[05-12-2023]-----Time:[12:59:34]\n"
}


def menu():
    print("-------------------------")
    print("1.Cashing out\n"
          "2.Transaction History\n"
          "3.Balance\n"
          "4.Return card\n"
          "-------------------------")
    choice=int(input("Select an index:"))
    if choice==1:
        return cashing_out()
    if choice == 2:
        return transaction_history()
    if choice == 3:
        return balance0()
    if choice == 4:
        exit("|--------------------------------------------|\n"
             "|Please take your card. Have a wonderful day!|\n"
             "|--------------------------------------------|")


def balance0():
    balance = user.get("balance")
    print("-----------------------")
    print(f"Your balance:{balance}$")
    print("-----------------------")
    input("Press enter to get back to main menu.")
    return menu()


def time():
    data = datetime.datetime.now()
    data = str(data).split()
    date = data[0].split("-")[::-1]
    date="-".join(date)
    time1 = data[1]
    time1 = time1.split('.')
    time1 = time1[0]
    return f'Date:[{date}]-----Time:[{time1}]'


def transaction_history():
    print('------------------------------------------------------------------')
    print(user.get("transactionHistory"))
    print('------------------------------------------------------------------')
    input("Press enter to get back to main menu.")
    return menu()


def cashing_out():
    balance=user.get("balance")
    print("------------------")
    print(f"Balance:{balance}$")
    print("------------------")
    amount=int(input("Enter the amount:"))
    if amount>balance:
        print("-----Insufficient balance-----")
        input("Press enter to continue.")
        return menu()
    user.update({"balance":balance-amount})
    user["transactionHistory"]+=f'Cashing out-{amount}$-----{time()}'
    list1 = [100, 50, 20, 10, 5, 1]
    list2 = [0, 0, 0, 0, 0, 0]
    for i in range(0, len(list1)):
        if amount / list1[i] >= 1:
            list2[i] = amount // list1[i]
            amount %= list1[i]
    print('----------------------------------------')
    for i in range(0, len(list1)):
        if list2[i] != 0:
            print(f'{list2[i]} pieces of {list1[i]}$')
    print('----------------------------------------')
    print("Please take your money.")
    input("Press enter to get back to main menu.")
    return menu()


def pin_check():
    pin0=int(input(f"Good day {user.get('name')+' '+user.get('surname')}! Please enter your pin:"))
    while True:
        if len(str(pin0))!=4:
            print("Pin must be 4 characters long.")
            pin0=int(input("Enter your pin again:"))
            continue
        if pin0==user.get("pin"):
            return menu()
        else:
            pin_wrong()


def pin_wrong():
    attempts=5
    while attempts>0:
        print(f"{attempts} attempts left.")
        pin1 = int(input("Pin is incorrect. Enter your pin again:"))
        while len(str(pin1))!=4:
            print("Pin must be 4 characters long.")
            pin1=int(input("Enter your pin again:"))
        if pin1==user.get("pin"):
            return menu()
        else:
            attempts-=1
    exit("|--------------------------------|\n"
         "|You entered too many wrong pins.|\n"
         "|--------------------------------|")


pin_check()

