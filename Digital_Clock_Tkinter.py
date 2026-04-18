import tkinter as tk
from time import strftime
from datetime import datetime

# Create main window
root = tk.Tk()
root.title("Digital Clock (12-hour)")
root.geometry("420x250")
root.resizable(False, False)
root.configure(bg="black")

# Time label
time_label = tk.Label(root, font=('calibri', 40, 'bold'), bg='black', fg='cyan')
time_label.pack(pady=5)

# Date label
date_label = tk.Label(root, font=('calibri', 18), bg='black', fg='white')
date_label.pack()

# Update function
def update_time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    current_date = datetime.now().strftime('%A, %d %B %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

update_time()
root.mainloop()
