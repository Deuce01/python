import tkinter as tk
from tkinter import ttk

class VideoCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encrypted Video Call")

        self.create_widgets()

    def create_widgets(self):
        self.label_path = ttk.Label(self.root, text="Enter the path for encrypted video call:")
        self.label_path.pack(pady=10)

        self.entry_path = ttk.Entry(self.root, width=40)
        self.entry_path.pack(pady=10)

        self.call_button = ttk.Button(self.root, text="Start Encrypted Video Call", command=self.start_video_call)
        self.call_button.pack(pady=20)

    def start_video_call(self):
        path = self.entry_path.get()
        # Placeholder for starting the encrypted video call using the specified path
        print(f"Starting encrypted video call to: {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCallApp(root)
    root.mainloop()
