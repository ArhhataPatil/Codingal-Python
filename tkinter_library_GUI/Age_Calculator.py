from tkinter import *
from datetime import date

window = Tk()
window.title("Age Calculator")
window.geometry("300x350")
window.config(bg="#0a1f44")

def calculate_age():
    Byear = int(entry_year.get())
    Bmonth = int(entry_month.get())
    Bday = int(entry_day.get())

    today = date.today()
    age = today.year - Byear

    if today.month < Bmonth:
        age -= 1
    elif today.month == Bmonth:
        if today.day < Bday:
            age -= 1

    result_label.config(text="Age: " + str(age))

Label(window, text="Day", bg="#0a1f44", fg="#a6c8ff").pack()
entry_day = Entry(window, bg="#d6e6ff")
entry_day.pack(pady=5)

Label(window, text="Month", bg="#0a1f44", fg="#a6c8ff").pack()
entry_month = Entry(window, bg="#d6e6ff")
entry_month.pack(pady=5)

Label(window, text="Year", bg="#0a1f44", fg="#a6c8ff").pack()
entry_year = Entry(window, bg="#d6e6ff")
entry_year.pack(pady=5)

Button(window, text="Calculate Age", bg="#1f4e8c", fg="white", command=calculate_age).pack(pady=15)

result_label = Label(window, text="", bg="#0a1f44", fg="white")
result_label.pack()

window.mainloop()