# Password Manager 

## Introduction 
The Password Manager is a Python application that uses tkinter library for the graphical user interface (GUI) and sqlite3 for database management. It is designed to store personal account information and has features for measuring password strength and generating random passwords. 

### Technologies Used (Languages)  
* Python (tkinter)
* SQLite (sqlite3)

## Features 
* **Secure Password Storage**: Safely store your account and password information (add, update and delete)
* **Search**: Find and retrieve stored account information 
* **Password Strength Meter**: Evaluate the strength of your passwords 
* **Password Generator**: Create random passwords based on selected preferences (length, uppercase and lowercase letters, numbers, and special characters)

## Getting Started 
To use the Password Manager, follow these steps: 
1. Clone this **Password_Manager** repository: `git clone https://github.com/acyc99/Password_Manager.git`
2. Download the [Common Password List ( rockyou.txt )](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt) and save it as **dictionary_pw.txt** to the project folder
3. Activate your virtual environment and run `python .\password_manager.py`
    * tkinter and sqlite3 are included in the Python standard library, so no installation is required

## Usage 
* Add, update, or delete account(s)
* Show all accounts stored in the database 
* Search account(s) by website and retrieve account information 
* Measure password strength 
* Generate strong password 

## References 
- [YouTube Tutorial Video -  Password Manager Using Tkinter](https://youtu.be/dEi_MCfhw5o?si=OYXwYRhrjiaIecWP) by Python Programming with Sanju 
- [YouTube Tutorial Video - Password Strength Checker in Python](https://youtu.be/iJ01q-sRJAw?si=6IOf3ThLTpTx7Mxs) by NeuralNine 