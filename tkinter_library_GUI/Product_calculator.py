from tkinter import *

window = Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")
window.config(bg="#f55f8a")

def calc():
    result_display.delete('1.0', END)
    try:
        a = float(e1.get())
        b = float(e2.get())
        product = a * b
        result_display.insert(END, "Product: " + str(product))
    except:
        result_display.insert(END, "Error: Enter numbers only")

Label(window, text="This app takes two numbers and finds their product.", bg="#f55f8a", fg="white").pack(pady=5)

Label(window, text="Enter First Number:", bg="#f55f8a", fg="white").pack()
e1 = Entry(window, bg="#f595a8")
e1.pack(pady=5)

Label(window, text="Enter Second Number:", bg="#f55f8a", fg="white").pack()
e2 = Entry(window, bg="#f595a8")
e2.pack(pady=5)

Button(window, text="Calculate Product", command=calc, bg="#1e90ff", fg="white").pack(pady=10)

result_display = Text(window, height=2, width=30, bg="#f595a8", fg="white")
result_display.pack(pady=10)

window.mainloop()