class Account:



    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# account=Account("balance.txt")
# print("Initial balance ", account.balance)
#
# account.withdraw(100)
# print("Balance after witdhraw", account.balance)
#
# account.commit()

jacks_checking = Checking("jack.txt", 1)
jacks_checking.transfer(10)
jacks_checking.commit()
print("Jack", jacks_checking.balance)


johns_checking = Checking("john.txt", 1)
johns_checking.transfer(10)
johns_checking.commit()
print("John", johns_checking.balance)

print(johns_checking.__doc__)