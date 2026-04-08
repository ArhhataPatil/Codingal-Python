from tkinter import *

window = Tk()
window.title("Product Calculator")
window.geometry("350x300")
window.config(bg="#f55f8a")

def calc():
    try:
        a = float(e1.get())
        b = float(e2.get())
        out.config(text="Product: " + str(a * b))
    except:
        out.config(text="Enter numbers only")

Label(window, text="Multiply Two Numbers", bg="#f595a8", fg="white").pack(pady=10)

e1 = Entry(window, bg="#f595a8")
e1.pack(pady=5)

e2 = Entry(window, bg="#f595a8")
e2.pack(pady=5)

Button(window, text="Calculate", command=calc, bg="#1e90ff", fg="#f595a8").pack(pady=10)

out = Label(window, fg="#f2bfc9", bg="#f55f8a")
out.pack(pady=10)

window.mainloop()