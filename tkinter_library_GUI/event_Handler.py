from tkinter import *

#create the main window
window= Tk()
window.title("Event Handler")
window.geometry("200x200")

def keyword(event):
    print("You pressed the key: " + event.char)
    
#bind the key press event to the keyword function
window.bind("<Key>", keyword)

def click(event):
    print("The button has been clicked")

button= Button(text= "Click here!")
button.pack()
button.bind("<Button-1>", click)




window.mainloop()