from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo


app = Tk()
app.title("Login")
app.geometry("400x400")


#subroutines

def create_account():
    with open('create_account.txt', 'a') as f:


        name = entrybox3.get()
        number = entrybox4.get()
        email = entrybox5.get()
        password = entrybox6.get()
        confirmed_password = entrybox7.get()
        if(len(password)!=8):
            showerror(title="Error", message="Password must be 8 characters long")
        elif(password!=confirmed_password):
            showerror(title="Error",message="Password does not match")
        else:

            f.write(name+"\n")
            f.write(number+"\n")
            f.write(email+"\n")
            f.write(confirmed_password+"\n")

            showinfo(title="Congratulations!!", message="You have successfully created your account")


def login():
    email1 = entrybox1.get()
    email2 = entrybox5.get()
    password1 = entrybox2.get()
    password2 = entrybox7.get()
    if(email1!=email2):
        showerror(title="Sorry", message="This Email-Id does not exists. Please create an account first.")
    elif(password1!=password2):
        showerror(title="Sorry", message="Wrong Password. Try Again")
    else:
        showinfo(title="Congratulations!!", message="You have successfully LOGGED IN")


#label/Frames

Label(app, text="LOGIN", font=16).grid(row=0, column=0, sticky=W)
first = Frame()
Label(first, text="Enter your Email-Id").grid(row=2, column=0, sticky=W)
Label(first, text="Enter your Password").grid(row=3, column=0, sticky=W)

first.grid(row=1, column=0, sticky=W)

Label(app, text="CREATE ACCOUNT", font=16).grid(row=2, column=0, sticky=W)


second = Frame()
second.grid(row=3, column=0, sticky=W)
Label(second, text="Enter your name").grid(row=3, column=0, sticky=W)
Label(second, text="Enter your Phone number").grid(row=4, column=0, sticky=W)
Label(second, text="Enter your Email-ID").grid(row=5, column=0, sticky=W)
Label(second, text="Create Password").grid(row=6, column=0, sticky=W)
Label(second, text="(Password must be 8 characters long)").grid(row=6, column=3, sticky=W)
Label(second, text="Confirm Password").grid(row=7, column=0, sticky=W)


#entry boxes for login:
entrybox1 = Entry(first,width=15, bg="light grey")
entrybox1.grid(row=2, column=2, sticky=W)
entrybox2 = Entry(first,bg="light grey", width=15, show="*")
entrybox2.grid(row=3, column=2, sticky=NW)

# Entry boxes for creating account:

entrybox3 = Entry(second, width=15, bg="light grey")
entrybox3.grid(row=3, column=2, sticky=W)
entrybox4 = Entry(second, width=15, bg="light grey")
entrybox4.grid(row=4, column=2, sticky=W)
entrybox5 = Entry(second, width=15, bg="light grey")
entrybox5.grid(row=5, column=2, sticky=W)
entrybox6 = Entry(second, width=15, bg="light grey", show="*")
entrybox6.grid(row=6, column=2, sticky=W)
entrybox7 = Entry(second, width=15, bg="light grey", show="*")
entrybox7.grid(row=7, column=2, sticky=W)



#buttons

Button(first, text="Login", command=login).grid(row=7, column=1, sticky=W)
Button(second, text="Create Account", command=create_account).grid(row=8, column=1, sticky=W)


app.mainloop()