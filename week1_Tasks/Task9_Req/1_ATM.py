# Req 1:
# ----------
# Create an ATM program with:
# Minimum balance as 5000 and the menu options should check balance, Deposit,Withdraw,Mini Statement and Exit options:
# Rules:
#     • User can perform multiple operations until Exit. 
#     • Withdrawal cannot exceed balance. 
#     • Deposit amount must be positive. 
#     • Store transaction history as a string. 
#     • Show all transaction in mini statements
#     • Maximum 3 incorrect PIN attempts. 
#     • Daily withdrawal limit.
 
def main():
    print("-----------------WELCOME TO THE AJ'S ATM-----------------")
    balance = 5000
    transactions = ""
    withdraw_amount=0
    
    # PIN CHECK (ALLOWED ONLY 3 ATTEMPTS)
    attempts = 0
    pin=0
    while attempts < 3:

        attempts+=1
        while True:
            try:
                pin = int(input("Enter the 4 digtit pin: "))
                break
            except Exception:
                print("enter the pin in digit")

        if pin == 1234:
            print("pin is correct")
            break
        elif attempts!=3:
            print("Enter the pin properly")

    else:
        print("you can't able to access the account . please try again later")
    
    if pin == 1234:
        while True:
            # OPTIONS FOR USERS 
            option = input ("Enter option menu : withdraw/deposit/balance/ministate/exit : ")

            match option:

                case "deposit":
                    while True:
                        amount = int(input("Enter the amount want to be credit : "))
                        if amount>0:
                            break
                        print("Enter the amount in positive")

                    balance+=amount
                    transactions += f"\n {amount} is credited."

                case "withdraw":

                    while True:
                        amount = int(input("Enter the amount want to be debited : "))

                        if amount <= 0:
                            print("Enter positive amount")
                            continue

                        elif amount > balance:
                            print(f"you dont have suffcient balance . Your balance amount is {balance}. please try to take amount below balance")
                            break

                        elif (withdraw_amount+amount) > 100000:
                            print("you cannot withdraw anymore you have reached the daily limit 100000")
                            break

                        elif balance-amount < 5000:
                            print(f"you can't able to withdraw 5000 or below . account should have minimum balance")
                            break

                        else:
                            balance-=amount
                            withdraw_amount +=amount
                            transactions += f"\n {amount} is debited."
                            break
    
                case "balance":
                    print(f"current balance is {balance}") 
                
                case "ministate":
                    print("---------------------Transaction history--------------------")
                    if transactions:
                        print(transactions)
                    else:
                        print("transaction not yet")

                case "exit":
                    print("Thanks for choosing our ATM ")
                    break

                case  _:
                    print("Enter the correctly again ")
        
main()
        



