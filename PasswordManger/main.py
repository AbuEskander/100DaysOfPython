from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def SavePassword():
    WebsiteLink = WebsiteInput.get()
    EmailLink = EmailInput.get()
    Password = PasswordInput.get()
    newData= {
        WebsiteLink:{
            "email":EmailLink,
            "Password":Password
        }
    }
   
    if not len(WebsiteLink) and not len(Password):
         messagebox.showwarning(title="Oops",message="Don't leave any field")   
    else:
        is_Ok = messagebox.askokcancel(title="Are you sure?" , message=f"These are the details entered:\nWebsite:{WebsiteLink}  \nEmail: {EmailLink}\nPassword: {Password}")
        if is_Ok:  
            with open("Passwords.json","w") as file:
                json.dump(newData,file,indent=4)
                WebsiteInput.delete(0,END)
                PasswordInput.delete(0,END)
    
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)
canvas=Canvas(width=200,height=200)
Image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=Image)

canvas.grid(column=1,row=0)

WebsiteLabel = Label(text="Website:",font=('Ariel', 10,"bold"))
WebsiteLabel.grid(column=0,row=1)

EmailLabel = Label(text="Email/UserName:",font=('Ariel', 10,"bold"))
EmailLabel.grid(column=0,row=2)

Password = Label(text="Password:",font=('Ariel', 10,"bold"))
Password.grid(column=0,row=3)

WebsiteInput = Entry(width=39)
WebsiteInput.focus()
WebsiteInput.grid(row=1,column=1,columnspan=2)

EmailInput = Entry(width=39)
EmailInput.insert(END,"basselawni1@gmail.com")
EmailInput.grid(row=2,column=1,columnspan=2)

PasswordInput = Entry(width=21)
PasswordInput.grid(row=3,column=1)

GeneratePassBtn = Button(text="Generate Password")
GeneratePassBtn.grid(column=2,row=3)

addBtn = Button(text="Add",width=36,command=SavePassword)
addBtn.grid(row=4,column=1,columnspan=2)
window.mainloop()
