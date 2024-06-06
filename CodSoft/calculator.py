from tkinter import *  

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def clear():
    entry.delete(0, END)

def add():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + " + ")

def subtract():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + " - ")

def multiply():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + " * ")

def divide():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + " / ")

def mod():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + " % ")


def equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Simple Calculator")
root.geometry("460x600") 
root.configure(bg="#2c2d2e")
entry = Entry(root, width=25 ,font=("",25) ,fg="#fff",bg="#2c2d2e",bd=0, )
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

button_1 = Button(root, text="1", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6,command=lambda: click(1))
button_2 = Button(root, text="2", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(2))
button_3 = Button(root, text="3", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(3))
button_4 = Button(root, text="4", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(4))
button_5 = Button(root, text="5", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(5))
button_6 = Button(root, text="6", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(6))
button_7 = Button(root, text="7", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(7))
button_8 = Button(root, text="8", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(8))
button_9 = Button(root, text="9", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6,command=lambda: click(9))
button_0 = Button(root, text="0", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#4d4d9a",width=6, command=lambda: click(0))

button_add = Button(root, text="+", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="black",activebackground="white",bg="#f3cbc5",width=6, command=add)
button_subtract = Button(root, text="-", padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="black",activebackground="white",bg="#f3cbc5",width=6, command=subtract)
button_multiply = Button(root, text="*",padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="black",activebackground="white",bg="#f3cbc5",width=6, command=multiply)
button_divide = Button(root, text="/",padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="black",activebackground="white",bg="#f3cbc5",width=6, command=divide)
button_mod = Button(root, text="%",padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="black",activebackground="white",bg="#f3cbc5",width=6, command=mod)

button_equal = Button(root, text="=",padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#1f862a",width=15, command=equal)
button_clear = Button(root, text="C",padx=5, pady=5, font=("arial",20,"bold"),bd=3,fg="#fff",activebackground="white",bg="#f4170b",width=6, command=clear)


# Put buttons on the screen

button_clear.grid(row=1, column=0,padx=3, pady=5)
button_mod.grid(row=1, column=1, padx=3, pady=5)
button_divide.grid(row=1, column=2, padx=3, pady=5)

button_multiply.grid(row=2, column=0 ,padx=3, pady=5)
button_subtract.grid(row=2, column=1 ,padx=3, pady=5)
button_add.grid(row=2, column=2 ,padx=3, pady=5)

button_7.grid(row=3, column=0 ,padx=3, pady=5)
button_8.grid(row=3, column=1 ,padx=3, pady=5)
button_9.grid(row=3, column=2 ,padx=3, pady=5)


button_4.grid(row=4, column=0 ,padx=3, pady=5)
button_5.grid(row=4, column=1 ,padx=3, pady=5)
button_6.grid(row=4, column=2 ,padx=3, pady=5)


button_1.grid(row=5, column=0 ,padx=3, pady=5)
button_2.grid(row=5, column=1 ,padx=3, pady=5)
button_3.grid(row=5, column=2 ,padx=3, pady=5)


button_0.grid(row=6, column=0 ,padx=3, pady=5)



button_equal.grid(row=6, column=1, columnspan=2 ,padx=3, pady=5)


root.mainloop()
