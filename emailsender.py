import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import smtplib
import schedule
import time

class EmailSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Email Sender")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TFrame", background="#334756")
        style.configure("TLabel", background="#334756", foreground="#ffffff", font=("Arial", 12))
        style.configure("TButton", background="#45aaf2", foreground="#ffffff", font=("Arial", 12))

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.label_to = ttk.Label(self.frame, text="To:")
        self.label_to.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.entry_to = ttk.Entry(self.frame, width=30)
        self.entry_to.grid(row=0, column=1, pady=(0, 5))

        self.label_subject = ttk.Label(self.frame, text="Subject:")
        self.label_subject.grid(row=1, column=0, sticky="w", pady=(0, 5))

        self.entry_subject = ttk.Entry(self.frame, width=30)
        self.entry_subject.grid(row=1, column=1, pady=(0, 5))

        self.label_body = ttk.Label(self.frame, text="Body:")
        self.label_body.grid(row=2, column=0, sticky="w", pady=(0, 5))

        self.text_body = tk.Text(self.frame, wrap=tk.WORD, width=30, height=5)
        self.text_body.grid(row=2, column=1, pady=(0, 10))

        self.label_schedule = ttk.Label(self.frame, text="Schedule (HH:MM):")
        self.label_schedule.grid(row=3, column=0, sticky="w", pady=(0, 5))

        self.entry_schedule = ttk.Entry(self.frame, width=30)
        self.entry_schedule.grid(row=3, column=1, pady=(0, 10))

        self.send_button = ttk.Button(self.frame, text="Schedule Email", command=self.schedule_email)
        self.send_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    def send_email(self):
        to_address = self.entry_to.get()
        subject = self.entry_subject.get()
        body = self.text_body.get("1.0", tk.END)

        try:
            with smtplib.SMTP("smtp.yourprovider.com", 587) as server:  # Replace with your email provider's SMTP server
                server.starttls()
                server.login("your_email@example.com", "your_password")  # Replace with your email and password
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail("your_email@example.com", to_address, message)  # Replace with your email
                messagebox.showinfo("Email Sent", "Email successfully sent!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def schedule_email(self):
        schedule_time = self.entry_schedule.get()

        try:
            hh, mm = map(int, schedule_time.split(':'))
            schedule.every().day.at(f'{hh:02d}:{mm:02d}').do(self.send_email)
            messagebox.showinfo("Email Scheduled", f"Email scheduled for {schedule_time}")
        except ValueError:
            messagebox.showwarning("Invalid Time", "Please enter a valid time in HH:MM format.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSchedulerApp(root)
    root.mainloop()
