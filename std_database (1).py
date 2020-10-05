#import modules

#import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Spinbox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu
from pp import backend

#CLASS for Front End UI

class stddatabase:
    def __init__(self,root):
        self.root=root
        self.root.title("Student DATABASE")
        self.root.geometry("1220x520")
        self.root.configure(bg="#cce3ed")
        
        std_date=StringVar()
        std_id=StringVar()
        std_name=StringVar()
        std_course=StringVar()
        std_batch=StringVar()
        std_attendance=IntVar() 
        
        ''''CREATE THE FRAMES'''
        
        mainframe=Frame(self.root,bg="#cce3ed")
        mainframe.grid()

        headframe = Frame(mainframe,bd=2,padx=30,pady=10,
                          bg="#b49de3",relief=RIDGE)
        headframe.pack(side=TOP)
        self.label1=Label(headframe,font=("Arial Bold",40),
                         text=' STUDENT ATTENDANCE ',bg='#96d9d4')
        self.label1.grid() 
        
        #creating Operation frame
        operationframe=Frame(mainframe,bd=3,width=1300,height=120,
                             padx=50,pady=20,bg="#97afdb",
                             relief=RIDGE)   
        operationframe.pack(side=RIGHT) 

        #creating Body Frame      
        bodyframe=Frame(mainframe,bd=2,width=1300,height=500,
                             padx=30,pady=20,bg="#a7b9db",
                             relief=RIDGE)  
        bodyframe.pack(side=BOTTOM)

        leftbodyframe=LabelFrame(bodyframe,bd=3,width=650,height=250,
                             padx=20,pady=10,bg="#a490d6",
                             relief=RIDGE,font=("Arial Bold",15),
                             text="STUDENT DETAILS")
        leftbodyframe.pack(side=LEFT)

        rightbodyframe=LabelFrame(bodyframe,bd=3,width=350,height=250,
                             padx=20,pady=10,bg="#a490d6",
                             relief=RIDGE,font=("Arial Bold",15),
                             text="STUDENT INFORMATION")
        rightbodyframe.pack(side=RIGHT)    

        '''Add WIDGETS to LEFT BODY FRAME'''

        self.label_date=Label(leftbodyframe,bd=2,text="DATE",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_date.grid(row=0,column=0,sticky=W) 

        self.entry_date=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_date)                                                                      
        self.entry_date.grid(column=1,row=0,sticky=W,padx=10)

        self.label_id=Label(leftbodyframe,bd=2,text="Student ID",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_id.grid(row=1,column=0,pady=10,sticky=W) 

        self.entry_id=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_id)                                                                      
        self.entry_id.grid(column=1,row=1,sticky=W,padx=10)
        
        self.label_name=Label(leftbodyframe,bd=2,text="Student NAME",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_name.grid(row=2,column=0,pady=1,sticky=W) 

        self.entry_name=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_name)                                                                      
        self.entry_name.grid(column=1,row=2,sticky=W,padx=10)

        self.label_course=Label(leftbodyframe,bd=2,text=" Course",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_course.grid(row=3,column=0,pady=10,sticky=W) 

        self.entry_course=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_course)                                                                      
        self.entry_course.grid(column=1,row=3,sticky=W,padx=10)
        
        self.label_batch=Label(leftbodyframe,bd=2,text="Batch",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_batch.grid(row=4,column=0,pady=10,sticky=W) 

        self.entry_batch=Entry(leftbodyframe,width=30,font=("Arial Bold",12),textvariable=std_batch)                                                                      
        self.entry_batch.grid(column=1,row=4,sticky=W,padx=10)

        self.label_attendance=Label(leftbodyframe,bd=2,text="Attendance",
                            font=("Arial Bold",12),padx=2,
                            fg="#255b9c",bg="white")
        self.label_attendance.grid(row=5,column=0,pady=10,sticky=W) 

       
        
        #Creating Radio Buttons for Attendance

        self.radio_button1=Radiobutton(leftbodyframe,value="PRESENT",text="PRESENT", 
                                       font=("Arial Bold",12),padx=2,fg="#0c5196",bg="white",variable=std_attendance)
        self.radio_button1.grid(column=1,row=5,sticky=W,padx=10)
        
        self.radio_button2=Radiobutton(leftbodyframe,value="ABSENT",text="ABSENT",
                                       font=("Arial Bold",12),padx=2,fg="#0c5196",bg="white",variable=std_attendance)
        self.radio_button2.grid(column=1,row=5,sticky=E,padx=10)

        '''Adding Widgets in Right Body Frame'''
        self.scroll=Scrollbar(rightbodyframe)
        self.scroll.grid(row=0,column=1,sticky=NS)

        self.productlist=Listbox(rightbodyframe,width=40,height=16,
                               font=("Arial Bold",12),
                               yscrollcommand=self.scroll.set)
        self.productlist.grid(row=0,column=0,padx=8)  
        self.scroll.config(command=self.productlist.yview) 

        '''Add The Buttons to OPERATION FRAME'''  
        
        self.add_button=Button(operationframe,text="ADD",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.add_button.grid(row=0,column=0,pady=10) 

        self.show_button=Button(operationframe,text="Show Data",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.show_button.grid(row=1,column=0,pady=10)

        self.clear_button=Button(operationframe,text="Clear",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.clear_button.grid(row=2,column=0,pady=10)

        self.delete_button=Button(operationframe,text="Delete",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.delete_button.grid(row=3,column=0,pady=10)

        self.search_button=Button(operationframe,text="Search",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.search_button.grid(row=4,column=0,pady=10)

        '''self.update_button=Button(operationframe,text="Update",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.update_button.grid(row=5,column=0,pady=10)'''

        self.close_button=Button(operationframe,text="Close",
                                font=("Arial Bold",12),bg="#00e2ff",
                                width=12,bd=3)
        self.close_button.grid(row=6,column=0,pady=10)



#BACKEND DATABASE OPERATIONS


if __name__=='__main__':
    root=Tk()
    application=stddatabase(root)
    root.mainloop()   