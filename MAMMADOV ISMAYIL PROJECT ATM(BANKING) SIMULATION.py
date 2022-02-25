import datetime
def parameters(accountants,passwords,balances):
    for a in range (0, 999999999):
        x="***+++ WELCOME TO MY ATM BANKING SYSTEM SIMULATION +++***"
        print(x.center(140))
        print(" ")
        entered_Name = input("Please, enter your name: ")
        entered_Name = entered_Name.lower()
        entered_password = 0000
        index = 0
        count = 0
        y="***+++Thank you for using my ATM BANKING SYSTEM!!!+++***"
        for name in accountants:
            if name == entered_Name:
                index = count
                entered_password = input("\nThen, please enter password: ")
            count += 1 
        if entered_password == passwords[index]:
            atm_system = True
        else:
            print("INVALID DATA!!!")
            atm_system = False
            continue
        if atm_system == True:
            print("\nYour current balance is:",balances[index])
            withdraw_or_deposite = input("\n1)Withdraw money(w).\n2)Deposite(d).\n3)Balance inqiury(i).\nPlease, select transaction type(w/d/i):")
            if withdraw_or_deposite == "w":
                amount_of_withdraw = input("\nPlease, enter amount of money you want to withdraw: ")
                try:
                    amount_of_withdraw = int(amount_of_withdraw)
                    if amount_of_withdraw > balances[index] :
                        raise
                except:
                    print("INVALID DATA!!!")
                    continue
                rest_of_balance = balances[index] - amount_of_withdraw
                balances.remove(balances[index])
                balances.insert(index,rest_of_balance)
                available_balance = print("\nYour present balance is: ", rest_of_balance)
            elif withdraw_or_deposite == "d":
                amount_of_deposite = input("\nPlease, enter the amount of money you want to deposite: ")
                try:
                    amount_of_deposite = int(amount_of_deposite)
                    if amount_of_deposite +  balances[index] >= 1000000:
                        raise
                except:
                    print("INVALID AMOUNT!!!")
                    continue
                rest_of_balance =balances[index]+amount_of_deposite
                balances.remove(balances[index])
                balances.insert(index,rest_of_balance)
                available_balance = print("Your present balance is: ",  rest_of_balance)
            elif withdraw_or_deposite == "i":
                t = input("\n1)On the screen(s).\n2)on the receipt(r).\nPlease enter type of balance enquire(s/r): ")
                if t == "s":
                    print(" ")
                    print(" ")
                    print(entered_Name.capitalize(), "your current balance is: ", balances[index])
                elif t == "r":
                    x = datetime.datetime.now()
                    x=str(x)
                    balances[index]=str(balances[index])
                    line = entered_Name + " "+ "balance:" + " " + balances[index]
                    width= len(line) + 25
                    print("+" + "-" * width + "+")
                    print("|" + " " * width + "|")
                    left = (width - len(line))//2
                    right = (width - len(line)) - left
                    print("|" + " " * left + line + " " * right + "|" )
                    print("|" + " " * width + "|")
                    print("|" + x.center(width) + "|")
                    print("|" + " " * width + "|")
                    print("+" + "-" * width + "+")
        print(" ")
        print(y.center(140))
        break
def bank():
    passwords = ["2606","1107","0502"]
    accountants = ["ismayil mammadov", "sehrin jafarova", "tamilla aliyeva"]
    balances = [85000, 420000, 174890]
    atm_system = False
    parameters(accountants,passwords,balances)
bank()

                    