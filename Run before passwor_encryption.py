from cryptography.fernet import Fernet

def generate_key():
    """Generate a new key and save it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(f"Generated Key: {key.decode()}")

# Run this to generate the key
generate_key()
