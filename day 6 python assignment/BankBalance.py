class BankAccount:
    def __init__(self, ownername, balance):
        self.ownername = ownername
        self.balance = balance

    def deposit(self):
        print("enter the amount to be deposited")
        dep = input()
        dep = int(dep)
        print("the amount deposited is", dep)
        self.balance = dep + self.balance
        print("available balance is", self.balance)


    def withdraw(self):
        with_draw = input("enter the amount to be withdrawn")
        with_draw = int(with_draw)
        if with_draw > self.balance:
            print("your balance is low")
        else:
            print("the amount withdrawn is: ", with_draw)
        remaining_balance = self.balance - with_draw
        print("your available balance is : ", remaining_balance)


atm = BankAccount("caleb", 1000)
print(atm.ownername)
print("your current balance is", atm.balance)
atm.deposit()
atm.withdraw()
