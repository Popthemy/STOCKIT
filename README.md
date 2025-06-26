# STOCK IT

**STOCK IT** is a simple command-line stock management application built with **Python (OOP)** and **SQLite**. It allows you to register or authenticate a user and perform basic CRUD operations on stock items such as adding new items and viewing the stock list.The application is easy to use and interactive via a text-based menu.

---

## ✨ Features

* 🔐 **User registration and authentication with password hashing**
* ➕ **Create** new stock items
* 👀 **Read** and list all stock items
* ❌ **Delete** items from the stock
* 💡 **Prompt-driven UI** — choose options like "Create User," "Authenticate," and manage stock once logged in.

---

## 🛠️ Tech Stack

* **Python 3.x** (OOP style code)
* **SQLite** (lightweight relational database)
* **Command-line interface** for interaction

---

## 📂 Project Structure

```
STOCK-IT/
├── main.py           # Entry point and user interaction
├── auth.py           # Handles user registration and login
├── stock.py          # Handles stock CRUD operations
├── models.py         # Contains the data models
├── database.db       # SQLite database file
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your machine
* SQLite (comes bundled with Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/STOCK-IT.git
   cd STOCK-IT
   ```
2. Run the app:

   ```bash
   python stock_home.py
   ```

---

## 🎮 Usage

1. On startup, you’ll see a prompt:

   ```
   -----------------------------------------------------
    Welcome to your favourite Stock taking app.
    Create user or log in or delete .
    -----------------------------------------------------

    🔐 Enter 0 to Login or 1 to create account :
   ```
2. After creating a new user or logging in, you'll have options to:

   * **Add new stock items**
   * **Delete stock items**
   * **Log out the program at any time.**

---

## 🤝 Contributions

Contributions, suggestions, and bug reports are welcome. Please feel free to open an issue or submit a pull request.

---