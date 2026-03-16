from tkinter import *
from datetime import date

#creat window
root= Tk()
root.title("Getting started with Widgets!")
root.geometry("400x400")
lbl=Label(text="Hello world!", fg="yellow", bg="pink", height=-1, width= 300)
name= Label(text="Enter your name: ", fg="blue", bg="white")
name_entry= Entry()

def display():
    name= name_entry.get()
    global message
    message= "Welcome to the aplication! \nTodays date is:"
    greet= "Hello " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box= Text(height=10)
btn= Button(text="Submit", command=display, height=3, bg= "lightblue", fg= "darkblue")
lbl.pack()
name.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()