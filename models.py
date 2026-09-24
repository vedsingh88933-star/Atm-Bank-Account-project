def create_initial_data():
    """Helper to generate initial dummy data if the DB is empty."""
    from storage import load_db, save_db
    db = load_db()
    if not db:
        dummy_data = {
            "1001": {"name": "Alice Smith", "pin": "1234", "balance": 1500.0, "history": []},
            "1002": {"name": "Bob Jones", "pin": "5678", "balance": 300.0, "history": []}
        }
        save_db(dummy_data)
