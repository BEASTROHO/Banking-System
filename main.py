import sys
from db_handler import DatabaseHandler
from encryption import AuthManager
from gui import BankingGUI

def initialize_system():
    try:
        # Load secure key for encryption (in real deployments, read from env/config)
        secret_key = "your-secure-app-key" #enter your encryption key

        # Initialize encryption manager
        auth = AuthManager(secret_key)

        # Initialize database connection
        db = DatabaseHandler()
        db.connect()

        # Start GUI application
        app = BankingGUI(database=db, auth_manager=auth)
        app.run()

    except Exception as e:
        print(f"[ERROR] System initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    initialize_system()
