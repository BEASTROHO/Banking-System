# 🧩 Module Reference — Banking System App

This document breaks down each script/module used in the application for clarity and onboarding.

---

## `main.py`
- Acts as the entry point for the entire application.
- Initializes encryption and database layers.
- Launches the Tkinter GUI and manages app flow.

## `gui.py`
- Handles user interaction screens including:
  - Login
  - Dashboard
  - Deposit/Withdraw
  - Transaction history
- Uses Tkinter for layout and message prompts.

## `db_handler.py`
- Establishes secure connection to MySQL using `mysql-connector-python`.
- Executes queries for account creation, balance update, and transaction logging.
- Implements SHA-256 password hashing and validation.

## `encryption.py`
- Provides AES-256 encryption and decryption for sensitive data.
- Verifies credentials securely using hashed comparisons.
- Encodes/decodes strings for storage and transfer integrity.

## `config.json`
- Holds static app configuration such as DB host, credentials, and secret key.
- Simplifies environment setup and encourages secure deployment practices.

## `requirements.txt`
- Lists all third-party dependencies:
  - `mysql-connector-python`
  - `pycryptodome`
  - `tk`
- Ensures quick environment installation with `pip install -r requirements.txt`.

## `README.md`
- Front-facing project documentation.
- Includes installation, features, architecture, and license info.
