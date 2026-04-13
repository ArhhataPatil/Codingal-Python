from tkinter import *
from tkinter import messagebox 

# SETTING UP MAIN WINDOW
root= Tk()
root.title("Dnomination Calculator")
root.configure(bg="lightblue")
root.geometry("650x400")
label1=Label(root, text="Welcome to denomination calculator applictaion!", font=("Arial", 14), bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

# FUNCTION TO OPEN THE MESSAGE BOX
def message():
    Mbox=messagebox.showinfo("Alert", "Do you want to calculate the denomination count")
    if Mbox=="ok":
        topwind()

# ADDING BUTTON ON MAIN WINDOW
button1= Button(root, text="Lets get STARTED!", command=message, font=("Arial", 12), bg="lightgreen")
button1.place(x=260, y=360)

# FUNCTION TO OPEN THE TOP LEVEL WINDOW
def topwind():
    top=Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="lightyellow")
    top.geometry("600x350+50+50")

    lbl1=Label(top, text="Enter total ammount", font=("Arial", 12), bg="lightyellow")
    entry= Entry(top)

    lbl2=Label(top, text="Here are the number of notes for each denomination", font=("Arial", 12), bg="lightyellow")

    l1=Label(top, text="2000", font=("Arial", 12), bg="lightyellow")
    l2=Label(top, text="500", font=("Arial", 12), bg="lightyellow")
    l3=Label(top, text="100", font=("Arial", 12), bg="lightyellow")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    # CALCULATE FUNCTION
    def calculator():
        try:
            amount=int(entry.get())
            note2000= amount//2000
            amount=amount%2000
            
            note500= amount//500
            amount=amount%500

            note100= amount//100
            amount=amount%100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)  

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    btn=Button(top, text="Calculate", command=calculator, font=("Arial", 12), bg="lightgreen")
    
    #placeing the widgets
    lbl1.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl2.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()    
