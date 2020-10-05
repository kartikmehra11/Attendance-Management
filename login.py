#import mysql.connector
from tkinter import *
#from tkinter.ttk import * 
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Spinbox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu


win=Tk()
win.title("Login")
win.geometry("430x300")
win.resizable(False,False)
win.configure(bg="#a490d6")

#Heading FRAME
mainframe=Frame(win,bg="#cce3ed")
mainframe.grid()

headframe = Frame(mainframe,bd=2,padx=30,pady=10,
                          bg="#b49de3",relief=RIDGE)
headframe.pack(side=TOP)
labelframe=Label(headframe,font=("Arial Bold",23),
                         text=' LOGIN PAGE ',bg='#96d9d4')
labelframe.grid()

#creating Operation frame
operationframe=Frame(mainframe,bd=3,width=150,height=150,
                             padx=30,pady=20,bg="#97afdb",
                             relief=RIDGE)   
operationframe.pack(side=BOTTOM) 
#Body FRAME
bodyframe=Frame(mainframe,bd=2,width=150,height=150,
                             padx=30,pady=20,bg="#a7b9db",
                             relief=RIDGE)  
bodyframe.pack(side=BOTTOM)



#Labels
label_name=Label(bodyframe,bd=2,text=" Username ",font=("Arial Bold",15),fg="#255b9c",bg="white")
label_name.grid(row=0,column=0,sticky=W,padx=20,pady=10) 

label_pass=Label(bodyframe,bd=2,text=" Password ",font=("Arial Bold",15),fg="#255b9c",bg="white")
label_pass.grid(row=1,column=0,sticky=W,padx=20,pady=10) 


#Entry Box
name_var=StringVar()
pass_var=StringVar()
entry_name=Entry(bodyframe,width=35,textvariable=name_var)
entry_name.grid(column=1,row=0,sticky=W)

entry_pass=Entry(bodyframe,show="*",width=35,textvariable=pass_var)
entry_pass.grid(column=1,row=1,sticky=W)


#submit button aftermath
def login_button():
    new_win1=Toplevel(win)
    new_win1.geometry("400x300")
    new_win1.title("!!LOGIN!!")
    new_win1.configure(bg="#cce3ed")
     
#submit button

submit_button=Button(operationframe,text="LOGIN",bg="#00e2ff",width=17,bd=3,padx=5,pady=5,font=("Arial Bold",13),command=login_button)
submit_button.grid(column=1,row=2,padx=0,pady=0,sticky=W)
#submit_button=Button(win,text="REGISTER",width=7,fg="Red",bg="Yellow",padx=10,pady=10,font=("Arial Bold",10),command=register_button)
#submit_button.grid(column=1,row=2,padx=0,pady=0,sticky=W)



win.mainloop()
