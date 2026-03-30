from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Virus Detector")
window.geometry("300x200")

def messageb():
    messagebox.showwarning("Virus Detector","ALERT! Virus Detected")

button= Button(window,text="Scan for Virus", command=messageb)
button.place(x=100, y=80)
window.mainloop()