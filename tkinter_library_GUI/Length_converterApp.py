from tkinter import *

# Create window
window = Tk()
window.title("Length Converter")
window.geometry("400x300")

# Function to convert inches to cm
def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=str(round(cm, 2)) + " cm")
    except:
        result_label.config(text="Invalid input")

# Main frame (center everything)
frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = Label(frame, text="Inches to Centimetres", font=("Arial", 16))
title_label.pack(pady=10)

# Input
entry = Entry(frame, width=20)
entry.pack(pady=5)

# Button
convert_button = Button(frame, text="Convert", command=convert)
convert_button.pack(pady=5)

# Output
result_label = Label(frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
window.mainloop()