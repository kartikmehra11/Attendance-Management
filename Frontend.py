from tkinter import *
from pp import backend

win = Tk()
win.geometry('410x250')
win.title("E-ttendance")
win.config(bg='#e0e0eb')

# Labels
l1 = Label(win, text="Date")
l1.grid(row=0, column=0)

l2 = Label(win, text="Name")
l2.grid(row=1, column=0)
l3 = Label(win, text="Roll No")
l3.grid(row=2, column=0)
l4 = Label(win, text="Course")
l4.grid(row=0, column=2)
l5 = Label(win, text="Batch")
l5.grid(row=1, column=2)
l6 = Label(win, text="Attendance")
l6.grid(row=2, column=2)
l1.config(bg='#e0e0eb')
l2.config(bg='#e0e0eb')
l3.config(bg='#e0e0eb')
l4.config(bg='#e0e0eb')
l5.config(bg='#e0e0eb')
l6.config(bg='#e0e0eb')

# Entry boxes
date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

name_text = StringVar()
e2 = Entry(win, textvariable=name_text)
e2.grid(row=1, column=1)

roll_text = StringVar()
e3 = Entry(win, textvariable=roll_text)
e3.grid(row=2, column=1)

course_text = StringVar()
e4 = Entry(win, textvariable=course_text)
e4.grid(row=0, column=3)

batch_text = StringVar()
e5 = Entry(win, textvariable=batch_text)
e5.grid(row=1, column=3)

attendance_text = StringVar()
e6 = Entry(win, textvariable=attendance_text)
e6.grid(row=2, column=3)

# scrollbar
sb = Scrollbar(win)
sb.grid(row=4, column=2, rowspan=10)

# Listbox
list = Listbox(win, height=8, width=35)
list.grid(row=4, column=0, columnspan=2, rowspan=10)

# attaching sb and list
list.config(yscrollcommand=sb.set)
sb.config(command=list.yview)


def delete():
    sel = list.curselection()[0]
    selected_row = list.get(sel)
    backend.remove(selected_row[0])
    list.delete(ACTIVE)


def insert():
    list.delete(0, END)
    for i in backend.insert(date_text.get(), name_text.get(), roll_text.get(), course_text.get(), batch_text.get(),
                            attendance_text.get()):
        list.insert(0, i)


def view():
    list.delete(0, END)
    for i in backend.view():
        list.insert(END, i)


def search():
    list.delete(0, END)
    for i in backend.find(date_text.get(), name_text.get(), roll_text.get(), course_text.get(), batch_text.get(),
                          attendance_text.get()):
        list.insert(END, i)


# buttons
b1 = Button(win, text="Add", width=12, command=insert)
b1.grid(row=3, column=3)

b2 = Button(win, text="Search", width=12, command=search)
b2.grid(row=4, column=3)

b3 = Button(win, text="Delete", width=12, command=delete)
b3.grid(row=5, column=3)

b4 = Button(win, text="View All", width=12, command=view)
b4.grid(row=6, column=3)

b5 = Button(win, text="Close", width=12, command=win.destroy)
b5.grid(row=7, column=3)

win.mainloop()
