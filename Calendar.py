import calendar
import tkinter as tk

def show_calendar():
    year = int(entry_year.get())
    cal_data = calendar.TextCalendar(calendar.SUNDAY)
    calendar_text = cal_data.formatyear(year)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, calendar_text)
    text_output.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Yearly Calendar")

# Create input label and entry widget for year
label_year = tk.Label(root, text="Enter Year:")
label_year.grid(row=0, column=0, padx=5, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=0, column=1, padx=5, pady=5)

# Create button to display calendar
button_show = tk.Button(root, text="Show Calendar", command=show_calendar)
button_show.grid(row=0, column=2, padx=5, pady=5)

# Create text widget to display calendar
text_output = tk.Text(root, height=20, width=40)
text_output.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
text_output.config(state=tk.DISABLED)

# Run the main event loop
root.mainloop()
