def atm():
    print("welcome to the ATM! ")
    pin = "1234"
    balance = 1000

    while True: 
        entered_pin = input("please Enter your 4-digit PIN or type 'exit to quit: ")
        
        if entered_pin == pin:
            print("\n1. Check Balance")
            print("2. Withdrawl Money")
            print("3. Deposit Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("\nWhat would you like to do? Enter the number: ")
            if choice == '1':
                print(f"\n Your current balance = ${balance}")

            elif choice =='2':
                amount = float(input("\nEnter the amount to withdraw: $"))
                if amount > balance:
                    print("\nInsufficent balance")
                else:
                    balance -= amount 
                    print(f"\n${amount} has been withdrawn. Remaining balance: ${balance}\n")
            elif choice == '3':
                amount = float(input("\nEnter the amount to Deposit: $"))
                balance += amount 
                print(f"\n${amount} has been deposited. Remaining balance: ${balance}\n")

            elif choice == '4':
                new_pin = input("\nEnter your new 4 digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("\n PIN changed successfully! \n")
                else: print("\nInvalid PIN format. PIN must be 4 digit number\n")

            elif choice == '5':
                print("Thank You for using the ATM! Goodbye")
                break


        elif entered_pin.lower() == 'exit':
            print("Thank You for exiting the ATM! Goodbye")
            break

        else:
            print("\nIncorrect PIN, please try again\n")


atm()