def main():
    balance = 5000
    withdraw_amount=0

    while True:
        option = input ("Enter option menu : withdraw/deposit : ")

        match option:

            case "deposit":
                while True:
                    try : 
                        amount = int(input("Enter the amount want to be credit : "))
                        if amount>0:
                            break
                        print("Enter the amount in positive")
                    except ValueError:
                        print("Invalid number!")
                balance+=amount
                
                print(f"deposited amount {amount} and current balance {balance}")
            
            case "withdraw":

                while True:
                    try:
                        amount = int(input("Enter the amount want to be debited : "))

                        if amount <= 0:
                            print("Enter positive amount")
                            continue

                        elif amount > balance:
                            print(f"you dont have suffcient balance . Your balance amount is {balance}. please try to take amount below balance")
                            continue
                        
                        elif balance-amount < 5000:
                            print(f"you can't able to withdraw 5000 or below . account should have minimum balance")
                            break

                        else:
                            balance-=amount
                            withdraw_amount +=amount
                            print(f"deposited amount {amount} and current balance {balance}")
                            break

                    except ValueError:
                        print("invalid number!")

main()
        



