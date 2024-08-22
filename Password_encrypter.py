from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

def load_key():
    """Load the previously generated key."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        messagebox.showerror("Key Error", "Key file not found. Please generate a key first.")
        return None

def encrypt_message(message):
    """Encrypt a message using the loaded key."""
    key = load_key()
    if key:
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message
    return None

def decrypt_message(encrypted_message):
    """Decrypt a message using the loaded key."""
    key = load_key()
    if key:
        f = Fernet(key)
        try:
            decrypted_message = f.decrypt(encrypted_message).decode()
            return decrypted_message
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt password. Error: {e}")
            return None
    return None

def encrypt_password():
    """Encrypt the password entered by the user."""
    password = entry_password.get()
    if password:
        encrypted_password = encrypt_message(password)
        if encrypted_password:
            result_var.set(encrypted_password.decode())
    else:
        messagebox.showwarning("Input Error", "Please enter a password.")

def decrypt_password():
    """Decrypt the encrypted password entered by the user."""
    encrypted_password = entry_encrypted.get()
    if encrypted_password:
        decrypted_password = decrypt_message(encrypted_password.encode())
        if decrypted_password:
            result_var.set(decrypted_password)
    else:
        messagebox.showwarning("Input Error", "Please enter an encrypted password.")

# Create the main window
root = tk.Tk()
root.title("Password Encryption/Decryption")

# Create and place widgets
tk.Label(root, text="Enter Password:").pack(padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(padx=10, pady=5)

tk.Button(root, text="Encrypt", command=encrypt_password).pack(padx=10, pady=5)

tk.Label(root, text="Enter Encrypted Password:").pack(padx=10, pady=5)
entry_encrypted = tk.Entry(root, width=50)
entry_encrypted.pack(padx=10, pady=5)

tk.Button(root, text="Decrypt", command=decrypt_password).pack(padx=10, pady=5)

result_var = tk.StringVar()
tk.Label(root, text="Result:").pack(padx=10, pady=5)
tk.Entry(root, textvariable=result_var, state="readonly", width=50).pack(padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
