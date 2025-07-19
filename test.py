# Step 1: Create a file name Pa3Basil (this will just be the script name)

# Step 2: Create a data structure for 8 users
users = {
    "Ik": {"pin": "1111", "balance": 1000},
    "Divine": {"pin": "2222", "balance": 2000},
    "Wealth": {"pin": "3333", "balance": 3000},
    "Jeffery": {"pin": "4444", "balance": 4000},
    "User5": {"pin": "5555", "balance": 5000},
    "User6": {"pin": "6666", "balance": 6000},
    "User7": {"pin": "7777", "balance": 7000},
    "User8": {"pin": "8888", "balance": 8000}
}

# Step 4: Create multiple functions

def check_balance(name):
    print(f"{name}, your current balance is: ₦{users[name]['balance']}")

def deposit(name):
    amount = float(input("Enter amount to deposit: ₦"))
    users[name]['balance'] += amount
    print(f"Deposit successful. New balance is: ₦{users[name]['balance']}")

def withdraw(name):
    amount = float(input("Enter amount to withdraw: ₦"))
    if amount > users[name]['balance']:
        print("Insufficient funds.")
    else:
        users[name]['balance'] -= amount
        print(f"Withdrawal successful. New balance is: ₦{users[name]['balance']}")

def transfer(name):
    receiver = input("Enter receiver's name: ")
    if receiver not in users:
        print("Receiver not found.")
        return
    amount = float(input("Enter amount to transfer: ₦"))
    if amount > users[name]['balance']:
        print("Insufficient funds.")
    else:
        users[name]['balance'] -= amount
        users[receiver]['balance'] += amount
        print(f"Transfer successful. You sent ₦{amount} to {receiver}. Your new balance is ₦{users[name]['balance']}")

# Step 5 & 6: Run program and test

def atm():
    print("=== Welcome to Python ATM Simulator ===")
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")

    if name in users and users[name]['pin'] == pin:
        print(f"\nLogin successful. Welcome, {name}!")
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Exit")

            choice = input("Select an option: ")
            if choice == "1":
                check_balance(name)
            elif choice == "2":
                deposit(name)
            elif choice == "3":
                withdraw(name)
            elif choice == "4":
                transfer(name)
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Invalid name or PIN.")

# Invoke the main function
atm()
