import mysql.connector
from mysql.connector import Error
from datetime import datetime
import hashlib

class DatabaseHandler:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='your_secure_password',
                database='banking_db'
            )
        except Error as err:
            raise Exception(f"[Database Error] Connection failed: {err}")

    def create_account(self, customer_id, name, password, initial_balance):
        cursor = self.connection.cursor()
        hashed_pass = self.hash_password(password)
        query = """
            INSERT INTO accounts (customer_id, name, password_hash, balance, created_at)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (customer_id, name, hashed_pass, initial_balance, datetime.now()))
        self.connection.commit()

    def get_user_password(self, customer_id):
        cursor = self.connection.cursor()
        query = "SELECT password_hash FROM accounts WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def deposit(self, customer_id, amount):
        cursor = self.connection.cursor()
        query = "UPDATE accounts SET balance = balance + %s WHERE customer_id = %s"
        cursor.execute(query, (amount, customer_id))
        self.log_transaction(customer_id, 'deposit', amount)
        self.connection.commit()

    def withdraw(self, customer_id, amount):
        cursor = self.connection.cursor()
        query_check = "SELECT balance FROM accounts WHERE customer_id = %s"
        cursor.execute(query_check, (customer_id,))
        result = cursor.fetchone()

        if not result or result[0] < amount:
            raise Exception("Insufficient funds or account not found.")

        query = "UPDATE accounts SET balance = balance - %s WHERE customer_id = %s"
        cursor.execute(query, (amount, customer_id))
        self.log_transaction(customer_id, 'withdraw', amount)
        self.connection.commit()

    def get_transaction_history(self, customer_id):
        cursor = self.connection.cursor(dictionary=True)
        query = """
            SELECT type, amount, timestamp
            FROM transactions
            WHERE customer_id = %s
            ORDER BY timestamp DESC
        """
        cursor.execute(query, (customer_id,))
        return cursor.fetchall()

    def log_transaction(self, customer_id, transaction_type, amount):
        cursor = self.connection.cursor()
        query = """
            INSERT INTO transactions (customer_id, type, amount, timestamp)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (customer_id, transaction_type, amount, datetime.now()))

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
