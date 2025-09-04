
# 🏦 ATM Banking System in Python

## 📖 Overview
This project simulates an **ATM (Automated Teller Machine)** system using Python.  
It provides essential banking operations such as balance inquiry, cash withdrawal, deposit, and transaction history.  

The program uses **file handling with `pickle`** to store and retrieve customer account data securely, mimicking a real banking system’s database.  

---

## 🛠️ Features
- 🔑 **Login / Sign-Up System** – Existing users can log in, and new users can create accounts.  
- 💰 **Balance Inquiry** – View current account balance with date & time.  
- 💵 **Withdraw Money** – Secure withdrawal with balance check and receipt printing.  
- 💳 **Deposit Money** – Add funds to account and update records.  
- 📜 **Transaction History** – Displays credit (deposits) and debit (withdrawals).  
- 💾 **Persistent Database** – Stores accounts in a `data.pkl` file using `pickle`.  
- ⚠️ **Security** – PIN authentication with 3 attempts for both account number and PIN.  

---

## 📂 Project Structure
```

atm-system/
│── ATM.py              # Main source code
│── data.pkl            # Database file (stores accounts)
│── README.md           # Documentation
│── LICENSE             # License file (MIT recommended)
│── .gitignore          # Ignore unnecessary files

````

---

## 🚀 Getting Started
### ✅ Prerequisites
- Python 3.x installed on your system.

### ▶️ Running the Program
```bash
python ATM.py
````

---

## 💻 Example Run

```
**********************
Welcome to ATM
**********************
Select the Option: 
1- Login
2- Sign Up
>>>>> 1

Enter the account number
123456789
Enter your pin:
1234

**********************
1-Balance Inquiry
2-Cash withdraw
3-Deposit money
4-Transaction history
5-Exit
**********************
Enter your choice : 1
Your Balance is: 5000 PKR
2025-09-04 12:30:25
```

---

## 📊 Explanation

* When a user logs in, they can select from multiple banking services.
* Each action updates the `data.pkl` database, ensuring changes persist between runs.
* Withdrawals check for sufficient funds, and deposits update balances.
* All transactions print a **receipt** with name, amount, and timestamp.

---

## 🚧 Future Improvements

* 🔐 Encrypt account PINs instead of storing them in plain text.
* 🌐 Add a **GUI interface** (Tkinter / PyQt).
* 📱 Extend to a **mobile-friendly app**.
* 🏦 Add support for **multiple bank accounts per user**.

---

## 🤝 Author

👨‍💻 **A.G. Hasan Zarook**
