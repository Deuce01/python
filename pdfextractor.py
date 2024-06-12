import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfFileWriter

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def extract_page():
    input_pdf = input_entry.get()
    output_pdf = output_entry.get()
    try:
        page_number = int(page_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid page number")
        return

    try:
        pdf_reader = PdfReader(input_pdf)
        if page_number < 1 or page_number > pdf_reader.len(reader.pages)():
            messagebox.showerror("Invalid page number", f"Please enter a page number between 1 and {pdf_reader.getNumPages()}")
            return

        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_number - 1))

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

        messagebox.showinfo("Success", f"Page {page_number} has been extracted to {output_pdf}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("PDF Page Extractor")

# Create and place the widgets
tk.Label(root, text="Select PDF file:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Page number:").grid(row=1, column=0, padx=10, pady=10)
page_entry = tk.Entry(root, width=10)
page_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(root, text="Output file:").grid(row=2, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Extract Page", command=extract_page).grid(row=3, column=0, columnspan=3, pady=20)

# Start the main event loop
root.mainloop()
