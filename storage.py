import json
import os

DB_FILE = 'data/accounts.json'

def load_db():
    """Reads account data from the JSON database."""
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({}, f)
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    """Writes account data back to the JSON database."""
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)
