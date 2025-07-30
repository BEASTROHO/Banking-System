import tkinter as tk
from tkinter import messagebox

class BankingGUI:
    def __init__(self, database, auth_manager):
        self.db = database
        self.auth = auth_manager
        self.root = tk.Tk()
        self.root.title("Banking System Portal")
        self.root.geometry("400x500")
        self.current_user = None

    def run(self):
        self.build_login_screen()
        self.root.mainloop()

    def build_login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=("Arial", 18)).pack(pady=20)
        username_entry = tk.Entry(self.root)
        password_entry = tk.Entry(self.root, show="*")
        username_entry.pack(pady=10)
        password_entry.pack(pady=10)

        def perform_login():
            user = username_entry.get()
            passwd = password_entry.get()
            stored_hash = self.db.get_user_password(user)
            if stored_hash and self.auth.verify_password(passwd, stored_hash):
                self.current_user = user
                self.build_dashboard()
            else:
                messagebox.showerror("Authentication Failed", "Invalid credentials")

        tk.Button(self.root, text="Login", command=perform_login).pack(pady=20)

    def build_dashboard(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 14)).pack(pady=15)

        tk.Button(self.root, text="Deposit", width=20, command=self.handle_deposit).pack(pady=10)
        tk.Button(self.root, text="Withdraw", width=20, command=self.handle_withdraw).pack(pady=10)
        tk.Button(self.root, text="View Transactions", width=20, command=self.view_transactions).pack(pady=10)
        tk.Button(self.root, text="Logout", width=20, command=self.build_login_screen).pack(pady=10)

    def handle_deposit(self):
        self.transaction_window("Deposit")

    def handle_withdraw(self):
        self.transaction_window("Withdraw")

    def transaction_window(self, mode):
        self.clear_window()
        tk.Label(self.root, text=f"{mode} Amount", font=("Arial", 14)).pack(pady=20)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack(pady=10)

        def process():
            try:
                amount = float(amount_entry.get())
                if mode == "Deposit":
                    self.db.deposit(self.current_user, amount)
                else:
                    self.db.withdraw(self.current_user, amount)
                messagebox.showinfo("Success", f"{mode} successful!")
                self.build_dashboard()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text=mode, command=process).pack(pady=15)
        tk.Button(self.root, text="Back", command=self.build_dashboard).pack(pady=5)

    def view_transactions(self):
        self.clear_window()
        tk.Label(self.root, text="Transaction History", font=("Arial", 14)).pack(pady=10)
        transactions = self.db.get_transaction_history(self.current_user)

        for tx in transactions:
            record = f"{tx['type'].capitalize()}: ₹{tx['amount']} — {tx['timestamp']}"
            tk.Label(self.root, text=record).pack()

        tk.Button(self.root, text="Back", command=self.build_dashboard).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
