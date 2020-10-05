from tkinter import *
import mysql.connector
from tkinter import messagebox


def find(date='', name='', roll='', course='', batch='', attendance=''):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Kartik@1", database="attendance")
    mycursor = mydb.cursor()
    s = f"select * from stinfo where date='{date}' OR name='{name}' OR rollno='{roll}' OR course='{course}' OR batch='{batch}' OR attendance='{attendance}'"
    mycursor.execute(s)
    result = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return result


def view():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Kartik@1", database="attendance")
    mycursor = mydb.cursor()
    s = "select * from stinfo"
    mycursor.execute(s)
    result = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return result


def insert(date, name, roll, course, batch, attendance):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Kartik@1", database="attendance")
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            f"insert into stinfo (date,name,rollno,course,batch,attendance) values ('{date}','{name}','{roll}','{course}','{batch}','{attendance}')")
        messagebox.showinfo("", "Values inserted")
    except Exception as e:
        # raise ValueError('Not enought values')
        print(e)

    mydb.commit()


def remove(id):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Kartik@1", database="attendance")
    mycursor = mydb.cursor()
    s = f"delete from stinfo where id ='{id}'"
    mycursor.execute(s)
    messagebox.showinfo("", "Values deleted")
    mydb.commit()
