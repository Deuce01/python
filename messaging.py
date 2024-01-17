from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import tkinter as tk
from tkinter import ttk

class SecureMessagingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Messaging App")

        self.create_widgets()

        # Placeholder for the shared key between users (in a real-world app, this should be handled securely)
        self.shared_key = self.derive_key(b"password")

    def create_widgets(self):
        self.label_message = ttk.Label(self.root, text="Enter your message:")
        self.label_message.pack(pady=10)

        self.entry_message = ttk.Entry(self.root, width=40)
        self.entry_message.pack(pady=10)

        self.send_button = ttk.Button(self.root, text="Send Message", command=self.send_message)
        self.send_button.pack(pady=20)

        self.label_received = ttk.Label(self.root, text="Received Message:")
        self.label_received.pack(pady=10)

        self.received_text = tk.Text(self.root, wrap=tk.WORD, width=40, height=5)
        self.received_text.pack(pady=10)

    def derive_key(self, password):
        # Key derivation function (KDF)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=b"salt",
            length=32,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt_message(self, message):
        # Encryption
        cipher = Cipher(algorithms.AES(self.shared_key), modes.CFB(b'0' * 16), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
        return base64.urlsafe_b64encode(ciphertext).decode()

    def decrypt_message(self, ciphertext):
        # Decryption
        cipher = Cipher(algorithms.AES(self.shared_key), modes.CFB(b'0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(base64.urlsafe_b64decode(ciphertext.encode())) + decryptor.finalize()
        return decrypted_message.decode()

    def send_message(self):
        message = self.entry_message.get()
        encrypted_message = self.encrypt_message(message)

        # In a real-world app, you'd send the encrypted message to the recipient
        # Here, we simulate the recipient receiving the message
        decrypted_message = self.decrypt_message(encrypted_message)
        self.received_text.delete(1.0, tk.END)
        self.received_text.insert(tk.END, decrypted_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureMessagingApp(root)
    root.mainloop()
