# Importing tkinter module
from tkinter import *  

# Importing random module
import random  


# Creating main window
root = Tk()  
root.title("Password Generated")  
root.geometry("500x350") 
root.configure(bg="#2c2d2e")

# Function to generate random password
def rand():
    password.delete(0, END)  # Clearing any existing password
    password_length = int(enter.get()) 
    my_password = ''  

    # Generating random characters and Inserting int0 password 
    for i in range(password_length):
        my_password += chr(random.randint(33, 122))  
    password.insert(0, my_password)  


# Creating label 
input_label = Label(root, text="Enter Number of Characters",font=("",12,"bold"),bg="#2c2d2e",fg="white")  
input_label.pack(pady=20)  
 
# Creating textbox to enter  
enter = Entry(root, font=("", 24)) 
enter.pack(pady=0, ) 

# Creating label
input_label = Label(root, text="Your Password",font=("",12,"bold"),bg="#2c2d2e",fg="white")  
input_label.pack(pady=20)  

# Creating textbox for password
password = Entry(root, font=("", 24)) 
password.pack(pady=0) 

# Creating button to generate password
generate = Button(root, text="Generate",font=("arial",15,"bold"),bd=3,fg="#fff",activebackground="white",bg="#1f862a",width=8,  command=rand)  
generate.pack( padx=50 ,pady=30)  


root.mainloop()  
