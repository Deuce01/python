from cryptography.fernet import Fernet
import json
import os
import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master_password, storage_file="passwords.json"):
        self.master_password = master_password
        self.storage_file = storage_file
        self.key = self.load_or_generate_key()
        self.passwords = self.load_passwords()

    def load_or_generate_key(self):
        key_file = "key.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as file:
                file.write(key)
            return key

    def load_passwords(self):
        try:
            with open(self.storage_file, "rb") as file:
                encrypted_data = file.read()
                fernet = Fernet(self.key)
                decrypted_data = fernet.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_passwords(self):
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(json.dumps(self.passwords).encode())
        with open(self.storage_file, "wb") as file:
            file.write(encrypted_data)

    def add_password(self, website, username, password):
        self.passwords[website] = {"username": username, "password": password}
        self.save_passwords()

    def get_password(self, website):
        return self.passwords.get(website, None)

    def list_websites(self):
        return list(self.passwords.keys())

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.master_password_label = tk.Label(master, text="Enter Master Password:")
        self.master_password_label.pack()

        self.master_password_entry = tk.Entry(master, show="*")
        self.master_password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        master_password = self.master_password_entry.get()
        password_manager = PasswordManager(master_password)

        if password_manager:
            self.master_password_label.destroy()
            self.master_password_entry.destroy()
            self.login_button.destroy()

            self.show_main_menu(password_manager)
        else:
            messagebox.showerror("Error", "Invalid master password!")

    def show_main_menu(self, password_manager):
        self.add_button = tk.Button(self.master, text="Add Password", command=lambda: self.show_add_password(password_manager))
        self.add_button.pack()

        self.get_button = tk.Button(self.master, text="Get Password", command=lambda: self.show_get_password(password_manager))
        self.get_button.pack()

        self.list_button = tk.Button(self.master, text="List Websites", command=lambda: self.show_list_websites(password_manager))
        self.list_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack()

    def show_add_password(self, password_manager):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Password")

        website_label = tk.Label(add_window, text="Website:")
        website_label.pack()

        website_entry = tk.Entry(add_window)
        website_entry.pack()

        username_label = tk.Label(add_window, text="Username:")
        username_label.pack()

        username_entry = tk.Entry(add_window)
        username_entry.pack()

        password_label = tk.Label(add_window, text="Password:")
        password_label.pack()

        password_entry = tk.Entry(add_window, show="*")
        password_entry.pack()

        save_button = tk.Button(add_window, text="Save", command=lambda: self.save_password(password_manager, website_entry.get(), username_entry.get(), password_entry.get()))
        save_button.pack()

    def save_password(self, password_manager, website, username, password):
        password_manager.add_password(website, username, password)
        messagebox.showinfo("Success", "Password added successfully!")

    def show_get_password(self, password_manager):
        get_window = tk.Toplevel(self.master)
        get_window.title("Get Password")

        website_label = tk.Label(get_window, text="Website:")
        website_label.pack()

        website_entry = tk.Entry(get_window)
        website_entry.pack()

        get_button = tk.Button(get_window, text="Get Password", command=lambda: self.get_password(password_manager, website_entry.get()))
        get_button.pack()

    def get_password(self, password_manager, website):
        stored_password = password_manager.get_password(website)
        if stored_password:
            messagebox.showinfo("Password", f"Username: {stored_password['username']}\nPassword: {stored_password['password']}")
        else:
            messagebox.showerror("Error", "Website not found!")

    def show_list_websites(self, password_manager):
        websites = password_manager.list_websites()
        if websites:
            messagebox.showinfo("Websites", "\n".join(websites))
        else:
            messagebox.showinfo("Websites", "No websites stored!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
