# all concept used till constructor


class ATM:
    bankName = "Aadi and python Bank"
    def __init__(self,name,pin,balance=0): #Constructor
        self.name = name
        self.pin = pin
        self.balance = balance

    def authenticate(self):
        enteredPin = int(input("Enter the pin"))
        if enteredPin == self.pin:
            print("Login SuccessFull")
            return True
        else:
            print("Login Failed")
            return False
        
    def deposit(self):
        amount = int(input("Enter the amount to deposit"))
        if amount>0:
            self.balance += amount
            print("Amount deposited successfully: ")
        else:
            print("Invalid Amount")

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw :"))
        if amount>0:
            if amount<self.balance:
                self.balance-= amount
                print("Amount withdrawn successfully: ")
            else:
                print("insufficient balance")
        else:
            print("Invalid Amount")

    def checkBalance(self):
        print("Your balance is :",self.balance)

    @classmethod
    def showBankName(cls):
        print("Welcome To ",cls.bankName)

    @staticmethod
    def bankRule():
        print("Bank Rules     .................")
        print("Minimum 10000 balance is required in your account")
        print("Adhar must be linked to your bank")


name = input("Enter your name")
balance = int(input("Enter your balance "))
pin = int(input("Enter your pin"))

account = ATM(name,pin,balance)
if account.authenticate():
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Bank Name")
        print("5. Bank Rules")
        print("6. Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            account.deposit()
        elif choice == 2:
            account.withdraw()
        elif choice == 3:
            account.checkBalance()
        elif choice == 4:
            ATM.showBankName()
        elif choice == 5:
            ATM.bankRule()
        elif choice == 6:
            print("Thank you for using our services")
            break
        else:
            print("Invalid Choice")
    else:
        print("Invalid PIN")







    

