# 5) Create a Bank account class with deposit, withdrawal, and balance display methods.
class Bank:
    def __init__(self,balance):
        self.bal = balance

    def deposit(self,amount):
        self.bal += amount

    def Withdraw(self,amount):
        self.bal-=amount

    def balance(self):
        return self.bal

def main():
    account = Bank(0)
    while True:
        choice = input("Enter the choice (dep/with/bal/exit) : ")
        match choice :
            case "dep":
                n=int(input("Enter the deposit amount: "))
                account.deposit(n)

            case "with":
                n=int(input("Enter the withdraw amount: "))
                account.Withdraw(n)

            case "bal":
                print(account.balance())

            case "exit":
                print("------------exit------------")
                break
        
main()






    
    

        