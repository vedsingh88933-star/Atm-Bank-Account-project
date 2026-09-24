from storage import load_db

def authenticate_user():
    db = load_db()
    print("\n--- Welcome to VITyarthi ATM ---")
    acc_num = input("Enter Account Number: ").strip()
    
    if acc_num not in db:
        print("Error: Account not found.")
        return None
        
    pin = input("Enter 4-Digit PIN: ").strip()
    if db[acc_num]["pin"] == pin:
        print(f"\nWelcome back, {db[acc_num]['name']}!")
        return acc_num
    else:
        print("Error: Incorrect PIN.")
        return None
