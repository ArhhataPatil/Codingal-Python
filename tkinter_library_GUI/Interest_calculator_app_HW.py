from tkinter import *
import math

window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")
window.configure(bg="dark green")

def calculate():
    p = float(principal.get())
    t = float(time.get())
    r = float(rate.get()) / 100

    # Simple Interest
    si = p * r * t

    # Compound Interest
    ci = p * ((1 + r) ** t) - p

    result.config(text=f"Simple Interest = ${si:.2f}\nCompound Interest = ${ci:.2f}")

Label(window, text="Interest Calculator", bg="dark green", fg="white",
      font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

Label(window, text="Principal", bg="dark green", fg="white").grid(row=1, column=0, pady=5)
principal = Entry(window)
principal.grid(row=1, column=1)

Label(window, text="Time (Years)", bg="dark green", fg="white").grid(row=2, column=0, pady=5)
time = Entry(window)
time.grid(row=2, column=1)

Label(window, text="Rate (%)", bg="dark green", fg="white").grid(row=3, column=0, pady=5)
rate = Entry(window)
rate.grid(row=3, column=1)

Button(window, text="Calculate", command=calculate,
       bg="white", fg="dark green").grid(row=4, column=0, columnspan=2, pady=15)

result = Label(window, text="", bg="dark green", fg="white", font=("Arial", 12))
result.grid(row=5, column=0, columnspan=2)

window.mainloop()