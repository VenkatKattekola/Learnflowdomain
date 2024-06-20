from cryptography.fernet import Fernet
def Key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as file:
        file.write(key)
def load():
    return open("secret.key","rb").read()
def encrypt(password,key):
    k=Fernet(key)
    return k.encrypt(password.encode())
def decrypt(encrypted_password,key):
    k=Fernet(key)
    return k.decrypt(encrypted_password.decode())
    
import sqlite3
def connectdb():
    return sqlite3.connect("passwords.db")
def table(c):
    with c:
        c.execute("""
                CREATE TABLE IF NOT EXISTS Pwd (
                  pw_id INTEGER primary key, 
                  category TEXT NOT NULL, 
                  p_name TEXT NOT NULL, 
                  pwd TEXT NOT NULL)
                 """)
def pwd_insert(c,category,p_name,pwd):
    with c:
        c.execute("insert into Pwd(category,p_name,pwd) values(?,?,?)",(category,p_name,pwd))
def pwd_retreive(c,category):
    with c:
        return c.execute("select p_name,pwd from Pwd where category=?",(category,)).fetchall()
import random
import string
def pwd_gen(length=10):
    Char=string.ascii_letters + string.digits + string.punctuation
    password=' '.join(random.choice(Char) for i in range(length))
    return password


import getpass
def main():
    Key()
    key=load()
    c=connectdb()
    table(c)
    while True:
        print("1. Generate a new password")
        print("2. Store a password")
        print("3. Retrieve passwords by category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter the length of the password: "))
            password = pwd_gen(length)
            print(f"Generated Password: {password}")
        
        elif choice == '2':
            category = input("Enter the category(Work/Banking/OTT): ")
            p_name = input("Enter the name: ")
            password = getpass.getpass("Enter the password(The password is invisible while entering): ")
            encrypted_password = encrypt(password, key)
            pwd_insert(c, category, p_name, encrypted_password)
            print("Password stored successfully.")

        elif choice == '3':
            category = input("Enter the category: ")
            passwords = pwd_retreive(c, category)
            for p_name, encrypted_password in passwords:
                password = decrypt(encrypted_password, key)
                print(f"Name: {p_name}, Password: {password}")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()