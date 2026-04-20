from tkinter import *

window = Tk()
window.title("Password Strength App")
window.geometry("400x400")
window.configure(bg="#f6fa99")

def check_password():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result.config(text="Strong", fg="light green")
    else:
        result.config(text="Very Strong", fg="dark green")

# Title colour changed here
Label(window, text="Password Strength Checker",
      font=("Arial", 16, "bold"),
      bg="white",
      fg="#f80767").pack(pady=20)

Label(window, text="Enter Password:",
      bg="white",
      font=("Arial", 12)).pack(pady=10)

entry = Entry(window, show="*", width=25, font=("Arial", 12))
entry.pack(pady=10)

Button(window, text="Check Strength",
       command=check_password,
       bg="#f6fa99", fg="#f80767").pack(pady=15)

result = Label(window, text="",
               bg="white",
               font=("Arial", 16, "bold"))
result.pack(pady=20)

window.mainloop()