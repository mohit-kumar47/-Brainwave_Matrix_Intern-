import time

print("Please insert your CARD")
time.sleep(2)
print("CARD INSERTED")

password = 7777
pin = int(input("Enter your pin: \n"))
balance = 1000

if pin == password:
    while True:
        print("""
            1 == Balance
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == Exit
        """)
        try:
            choice = int(input("Enter your choice: \n"))
            if choice == 1:
                print(f"Your balance is: {balance}")
                print("========================================================================")
            elif choice == 2:
                withdraw = int(input("Enter the amount you want to withdraw: \n"))
                if withdraw > balance:
                    print("Insufficient balance")
                else:
                    balance -= withdraw
                    print(f"{withdraw} is withdrawn from your account.")
                    print(f"Your updated balance is: {balance}")
                print("========================================================================")
            elif choice == 3:
                deposit = int(input("Enter the amount you want to deposit: \n"))
                balance += deposit
                print(f"{deposit} is credited to your account.")
                print(f"Your updated balance is: {balance}")
                print("========================================================================")
            elif choice == 4:
                print("Thank you for using our services")
                break
            else:
                print("Invalid choice")
                print("========================================================================")
        except ValueError:
            print("Invalid input, please enter a number.")
            print("========================================================================")
else:
    print("Wrong pin, please try again.")
