import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image
from io import BytesIO

class QrCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Variables for input fields
        self.text_var = tk.StringVar()
        self.link_var = tk.StringVar()
        self.image_path_var = tk.StringVar()

        # Input fields
        tk.Label(root, text="Text:").pack()
        tk.Entry(root, textvariable=self.text_var).pack()

        tk.Label(root, text="Link:").pack()
        tk.Entry(root, textvariable=self.link_var).pack()

        tk.Label(root, text="Image Path:").pack()
        tk.Entry(root, textvariable=self.image_path_var).pack()

        # Buttons
        tk.Button(root, text="Generate Text QR Code", command=self.generate_text_qr).pack()
        tk.Button(root, text="Generate Link QR Code", command=self.generate_link_qr).pack()
        tk.Button(root, text="Generate Image QR Code", command=self.generate_image_qr).pack()

    def generate_text_qr(self):
        data = self.text_var.get()
        self.generate_qr_code(data)

    def generate_link_qr(self):
        data = self.link_var.get()
        self.generate_qr_code(data)

    def generate_image_qr(self):
        image_path = self.image_path_var.get()
        if image_path:
            with open(image_path, 'rb') as file:
                data = file.read()
                self.generate_qr_code(data)
        else:
            messagebox.showerror("Error", "Please provide a valid image path.")

    def generate_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Display the generated QR code image
        img.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = QrCodeGeneratorApp(root)
    root.mainloop()
