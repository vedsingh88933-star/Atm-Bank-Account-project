from models import create_initial_data
from auth import authenticate_user
from operations import check_balance, process_transaction, view_statement

def main():
    create_initial_data() # Seed database if empty
    
    current_account = None
    while current_account is None:
        current_account = authenticate_user()
        
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Mini Statement")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            check_balance(current_account)
        elif choice == '2':
            try:
                amt = float(input("Enter amount to withdraw: $"))
                process_transaction(current_account, amt, "withdraw")
            except ValueError:
                print("Error: Invalid number format.")
        elif choice == '3':
            try:
                amt = float(input("Enter amount to deposit: $"))
                process_transaction(current_account, amt, "deposit")
            except ValueError:
                print("Error: Invalid number format.")
        elif choice == '4':
            view_statement(current_account)
        elif choice == '5':
            print("Thank you for using VITyarthi ATM. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
