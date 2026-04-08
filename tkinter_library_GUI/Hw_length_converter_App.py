from tkinter import *

window= Tk()
window.title("Length Converter")
window.geometry("400x400")

frame= Frame(window, relief="sunken", width=350, height=200, bg="#FFB6C1")
label= Label(frame, text="Enter the length in inches:", bg="#6F4E37", fg="#FFB6C1", width=25)
entry= Entry(frame)


def display():
    inches= entry.get()
    cm= float(inches)*2.54
    message="The length in cm is: "
    textbox.insert(END, message)
    textbox.insert(END, cm)

textbox= Text(bg="#6F4E37", fg="#FFB6C1")
button= Button(frame, text="Convert to cm", bg="#6F4E37", fg="#6F4E37",command=display)


frame.place(x=30, y=30)
label.place(x=60, y=20)
entry.place(x=90, y=70)
button.place(x=120, y=120)
textbox.place(y=250)
window.mainloop()