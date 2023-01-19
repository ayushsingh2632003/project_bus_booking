from tkinter import *
from tkinter.messagebox import *

import sqlite3
con=sqlite3.Connection('database_for_bus_project')
cur=con.cursor()
cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_i number,route_id number,foreign key(operator_i) references operator(operator_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(Bus_id number,date date ,seatavaible number,PRIMARY KEY(Bus_id,date))')
cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number)')










root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
fr=Frame(root)

fr.grid(row=0,column=0,columnspan=10)


img_bus=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\\Desktop\\images_for_project\\Bus_for_project.png')
Label(fr,image=img_bus).grid(row=0,column=2,padx=w//2.5,columnspan=12)

Label(fr,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=25,columnspan=5)

Label(fr,text="ADD BUS ROUTE DETAILS ",font=('arial',15,'bold'),fg='blue',bg='WHITE').grid(row=2,column=2,padx=w//2.4)


fr2=Frame(root)
fr2.grid(row=1,column=3,pady=50)


Label(fr2,text="ROUTE ID",font=('arial',10,'bold')).grid(row=1,column=2)
route_id=Entry(fr2)
route_id.grid(row=1,column=3,padx=30)

Label(fr2,text="STATION NAME",font=('arial',10,'bold')).grid(row=1,column=4)
sname=Entry(fr2)
sname.grid(row=1,column=5,padx=30)

Label(fr2,text="STATION ID",font=('arial',10,'bold')).grid(row=1,column=6)
sid=Entry(fr2)
sid.grid(row=1,column=7,padx=30)


def add_route():
    if len(route_id.get())!=0 or len(sname.get())!=0 or len(sid.get())!=0:
        y=(route_id.get(),sname.get(),sid.get())
        query=('insert into route(route_id,station_name,station_id) values(?,?,?)')
        cur.execute(query,y)
        con.commit()
        showinfo("add route","BUS route ADDED SUCCESSFULLY")
        cur.execute('select * from route')
        res=cur.fetchall()
        print(res)
    else:
        showerror("value missing","all fields must be filled")


def delete_route():
    if len(route_id.get())!=0 or len(sname.get())!=0 or len(sid.get())!=0:
        y=(route_id.get(),sname.get(),sid.get())
        query='select * from route where route_id=? and  station_name=? and station_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            showinfo("delete","mentioned record removed successfully")
            y=(route_id.get(),sname.get(),sid.get())
            query='delete from route where route_id=? and station_name=? and  station_id=?'
            cur.execute(query,y)
            result=cur.fetchall()
            print(result)
        else:
            showerror("oops!!","no record found")
        showinfo("delete","deleted successfully")
        print(res)

    else:
        showerror("value missing","all fields must be filled")

    con.commit()

        
        

Button(fr2,text="ADD ROUTE",command=add_route,font=('arial',10,'bold'),bg='light green',fg='green').grid(row=1,column=8,padx=10)
Button(fr2,text="DELETE ROUTE",command=delete_route,font=('arial',10,'bold'),bg='red',fg='white').grid(row=1,column=9,padx=10,columnspan=2)

def home():
    root.destroy()
    import page2_
img_home=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\Desktop\\images_for_project\\home.png')
Button(fr2,image=img_home,command=home).grid(row=1,column=11)

