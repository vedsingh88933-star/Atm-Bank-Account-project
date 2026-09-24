from storage import load_db, save_db
from datetime import datetime

def check_balance(acc_num):
    db = load_db()
    print(f"\nCurrent Balance: ${db[acc_num]['balance']:.2f}")

def process_transaction(acc_num, amount, t_type):
    db = load_db()
    if t_type == "withdraw":
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
        if db[acc_num]['balance'] < amount:
            print("Error: Insufficient funds.")
            return
        db[acc_num]['balance'] -= amount
        
    elif t_type == "deposit":
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
        db[acc_num]['balance'] += amount
        
    # Log transaction
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {t_type.capitalize()} | ${amount:.2f}"
    db[acc_num]['history'].append(log_entry)
    
    save_db(db)
    print(f"\nSuccess: ${amount:.2f} {t_type}ed.")
    check_balance(acc_num)

def view_statement(acc_num):
    db = load_db()
    print("\n--- Recent Transactions ---")
    history = db[acc_num].get('history', [])
    if not history:
        print("No recent transactions.")
    else:
        for record in history[-5:]: # Show last 5
            print(record)
