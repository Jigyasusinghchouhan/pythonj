#bankAccount.py
class BankAccount():
    # Default Values for Account Details
    counter = 0
    basic_salary = 0
    total_salary = 0
    pf = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.counter += 1

    def deposit(self, amount): 
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

    def find_interest(self):
        interest = (self.balance * 0.05) 
        self.balance += interest

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: ${self.balance}"

    @classmethod
    def fromString(cls, data_str):
        lst = data_str.split()
        return cls(lst[0], float(lst[1]))

    @classmethod
    def fromList(cls, data_list):
        return cls(data_list[0], data_list[1])

    @classmethod
    def fromDict(cls, data_dict):
        return cls(list(data_dict.keys())[0], list(data_dict.values())[0])

    @staticmethod
    def display_details(acct):
        print(acct)
        print(f"basic_salary: {BankAccount.basic_salary}")
        print(f"total_salary: {BankAccount.total_salary}")
        print(f"pf: {BankAccount.pf}")
        print(f"No. of accounts created :{BankAccount.counter}")

#create account
acct1 = BankAccount('Jose',100)

#deposit
acct1.deposit(150)

#withdraw
acct1.withdraw(75)

#display details
BankAccount.display_details(acct1)

#Add counter for an accounts
BankAccount.counter += 1

#Print all account details
print(acct1)

# Find the interest amount and add it to the account balance
acct1.find_interest()
print(acct1)

#Take account details from the class object, string, list, and dictionary (Use class method)
data_str = "Steve 50"
acct2 = BankAccount.fromString(data_str)
print(acct2)

data_list = ["Dave", 100]
acct3 = BankAccount.fromList(data_list)
print(acct3)

data_dict = {"Alex":200}
acct4 = BankAccount.fromDict(data_dict)
print(acct4)