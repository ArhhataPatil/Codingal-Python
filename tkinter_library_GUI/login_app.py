from tkinter import *

#create window 
root= Tk()
root.title("Login App")
root.geometry("400x400")

#Create the frame
frame=Frame(master=root, width=350, height=200, bg="yellow")

lbl1= Label(frame, text="Username: ", bg="Yellow", fg="Blue", width=10)
lbl2=Label(frame, text="Email: ", bg="Yellow", fg="Blue", width=10)
lbl3=Label(frame, text="Password", bg="Yellow", fg="Blue", width=10)

#Use the entry widget to create text boxes for the user to enter details
name_entry= Entry(frame)
email_entry= Entry(frame)
pass_entry= Entry(frame, show="*")

def display():
    name=name_entry.get()
    greet="Hey! "+name
    message="\nCongratulations! You have successfully created an account."
    textbox.insert(END, greet)
    textbox.insert(END, message)


#Textbox to display the message
textbox=Text(bg="Red", fg="navyblue")

#add button to submit the details
btn=Button(text="Submit", command=display, bg="lightblue", fg="navyblue")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=150, y=180)
textbox.place(y=220)
root.mainloop()


