from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master = root, height = 200, width = 360, bg = "light pink")

lbl1 = Label(frame, text = "Full Name", bg = "blue", fg = "white", width = 12)
lbl2 = Label(frame, text = "Email Id", bg = "blue", fg = "white", width = 12)
lbl3 = Label(frame, text = "Enter Password", bg = "blue", fg = "white", width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = "*")

def display():
    name = name_entry.get()
    greet = "Hey"  + name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg = "light pink", fg = "black")
btn = Button(text = "Create Account", command = display, bg = "red")

frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 80)
email_entry.place(x = 150, y = 80)
lbl3.place(x = 20, y = 140)
pass_entry.place(x = 150, y = 140)
btn.place(x = 130, y = 210)
textbox.place(y = 250)

root.mainloop()