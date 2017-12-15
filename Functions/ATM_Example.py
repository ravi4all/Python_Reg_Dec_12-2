def userLogin(total_balance):
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Successfull...")
        options(total_balance)
    else:
        print("Login Failed...")

def withdraw(total_balance):
    amount = int(input("Enter the amount you want to withdraw : "))
    if amount > total_balance:
        print("Not sufficient balance...")
    else:
        total_balance = total_balance - amount
        # print("Available balance is",avail_bal)
    return total_balance

def deposit(total_balance):
    amount = int(input("Enter the amount you want to deposit : "))
    if amount > 5000:
        print("Amount should be less than 5000")
    else:
        total_balance = total_balance + amount
        # print("Available balance is",avail_bal)
    return total_balance

def bal_enquiry(total_balance):
    return total_balance

def options(total_balance):
    print("""
    1. Withdraw
    2. Deposit
    3. Balance Enquiry
    """)

    userChoice = int(input("Enter your choice : "))

    if userChoice == 1:
        total_balance = withdraw(total_balance)
        print("Current balance :",total_balance)
    elif userChoice == 2:
        total_balance = deposit(total_balance)
        print("Current balance :",total_balance)
    elif userChoice == 3:
        print("Available balance :",bal_enquiry(total_balance))
    else:
        print("Wrong Choice...")

def main():
    total_balance = 25000
    while True:
        userLogin(total_balance)
main()
