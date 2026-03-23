from tkinter import *
root= Tk()
root.title("Mini Product Calculator")
root.geometry("400x400")
lbl=Label(text="Enter your first number: ", fg="pink", bg="yellow")
entry1= Entry()
lbl2=Label(text="Enter your second number: ", fg="red", bg="blue")
entry2= Entry()
btn= Button(text="Calculate")       



lbl.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
btn.pack()
root.mainloop()