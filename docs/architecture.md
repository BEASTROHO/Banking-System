---

## `architecture.md` — System Design Overview

```md
# 🧠 Architecture Overview — Banking System App

This document describes the internal design and interaction flow of the Secure Banking System App, built using Python, MySQL, AES encryption, and Tkinter GUI.

---

## 📦 Module Breakdown

- `main.py`: Launches GUI and orchestrates user navigation.
- `gui.py`: Manages visual components—login, register, transactions.
- `encryption.py`: Encrypts and decrypts sensitive user inputs.
- `db_handler.py`: Interfaces with `banking_db` for queries and updates.
- `config.json`: Stores database credentials and app secrets.
- `requirements.txt`: Lists dependencies for setting up the environment.

---

## 🔁 Data Flow

1. **User Input via GUI**  
   → `gui.py` captures credentials / actions

2. **Encryption Layer**  
   → `encryption.py` encrypts sensitive data (e.g., passwords)

3. **Database Transaction**  
   → `db_handler.py` handles SQL operations securely

4. **UI Update**  
   → `gui.py` refreshes balance / history view in real-time

---

## 🔐 Security Layers

- AES encryption with `pycryptodome` for all credential handling.
- Config-managed secrets for better environment isolation.
- SQL injection avoided through parameterized queries.

---

## 🔧 Scalability Suggestions

- Move config to `.env` using `python-dotenv` for enhanced security.
- Add exception logging via `logging` module.
- Modularize GUI into separate screens/components for large-scale UIs.

---

## 📊 Diagram (Textual)

```
[GUI] → [Encryption] → [DB Handler] → [MySQL]
   ↑                                 ↓
[GUI Updates] ← [Balance / History ← Database]
```


