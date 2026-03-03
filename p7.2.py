balance = 0

def show():
    print("Current Balance:", balance)

def deposit(a):
    global balance
    balance += a
    print("Amount Deposited")

def withdraw(a):
    global balance
    if a <= balance:
        balance -= a
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

while True:
    print("\n1.Show  2.Deposit  3.Withdraw  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 4:
        break

    if ch == 1:
        show()
    elif ch == 2:
        a = int(input("Enter amount: "))
        deposit(a)
    elif ch == 3:
        a = int(input("Enter amount: "))
        withdraw(a)