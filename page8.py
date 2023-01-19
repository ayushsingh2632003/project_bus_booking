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


img_bus=PhotoImage(file='.\\Bus_for_project.png')
Label(fr,image=img_bus).grid(row=0,column=2,padx=w//2.5,columnspan=12)

Label(fr,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=25,columnspan=5)

Label(fr,text="ADD BUS DETAILS ",font=('arial',15,'bold'),fg='blue',bg='WHITE').grid(row=2,column=2,padx=w//2.4)



fr2=Frame(root)
fr2.grid(row=1,column=3,pady=20)
##
##def get_bus_id(bus_id_input,bus_type,input_capacity_var,input_route_id):
##    cur.execute("insert into operator values()")
    





Label(fr2,text="BUS ID",font=('arial',10,'bold')).grid(row=1,column=2,padx=5)
bus_id=Entry(fr2,width=15)
bus_id.grid(row=1,column=3,padx=5,pady=10)


Label(fr2,text="BUS TYPE").grid(row=1,column=4,padx=5)
bus_type=StringVar()
bus_type.set("SELECT BUS TYPE")
opt=['AC 3X2','NON AC 3X2','AC 2X2','NON AC 2X2','AC SLEEPER']

d_menu=OptionMenu(fr2,bus_type,*opt).grid(row=1,column=5,padx=5)

Label(fr2,text="CAPACITY ",font=('arial',10,'bold')).grid(row=1,column=6)
capacity=Entry(fr2,width=10)
capacity.grid(row=1,column=7,pady=10)

Label(fr2,text="FARE RS",font=('arial',10,'bold')).grid(row=1,column=8)

fare=Entry(fr2,width=15)
fare.grid(row=1,column=9,pady=10)
Label(fr2,text="OPERATOR ID",font=('arial',10,'bold')).grid(row=1,column=10,padx=17)
operator_id=Entry(fr2,width=10)
operator_id.grid(row=1,column=11,pady=10)

Label(fr2,text="ROUTE ID",font=('arial',10,'bold')).grid(row=1,column=12,padx=17)
route_id=Entry(fr2,width=10)
route_id.grid(row=1,column=13,pady=10)

def add_bus():
    if len(operator_id.get())!=0 or len(bus_id.get())!=0 or len(bus_type.get())!=0 or len(capacity.get())!=0 or len(fare.get())!=0 or len(route_id.get())!=0:
        y=(bus_id.get(),bus_type.get(),capacity.get(),fare.get(),operator_id.get(),route_id.get())
        query=('insert into bus(Bus_id ,type ,capacity,fare, operator_i,route_id) values(?,?,?,?,?,?)')
        cur.execute(query,y)
        con.commit()
        
        
        showinfo("add bus","bus added successfully")
        cur.execute('select * from bus')
        result=cur.fetchall()
        print(result)
    else:
        showerror("value missing","all fields must be filled")

        
def edit_bus():
    if len(operator_id.get())!=0 or len(route_id.get())!=0 or len(fare.get())!=0 or len(capacity.get())!=0 or len(bus_id.get())!=0:
        y=(bus_id.get())
        query='select * from bus where bus_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            showinfo("found!! ",'record found and edited')
            y=(bus_type.get(),capacity.get(),fare.get(),operator_id.get(),route_id.get(),bus_id.get())
            query='update bus set type=? ,capacity=?,fare=?,operator_i=?,route_id=? where bus_id=?'
            cur.execute(query,y)
            con.commit()
            result=cur.fetchall()
            print(result)
        else:
            showerror("oops!!","no record found")
        print(res)
        showinfo("bus edit","Bus record edited successfully")
    else:
        showerror("value missing","all fields must be filled")
        
    con.commit
    
    
    
def home():
    root.destroy()
    import page2_

add_bus_button=Button(fr2,text="ADD BUS",command=add_bus,height=1,font=('arial',15,'bold'),bg='light green',fg='black')


add_bus_button.grid(row=4,column=8,padx=20,pady=20)
edit_bus_button=Button(fr2,text="EDIT BUS",command=edit_bus,height=1,font=('arial',15,'bold'),bg='light green',fg='black')

edit_bus_button.grid(row=4,column=7,pady=20)
img_home=PhotoImage(file='.\\home.png')
home=Button(fr2,image=img_home,command=home)
home.grid(row=4,column=9,pady=80)
root.bind('<KeyPress>',home)

root.mainloop()
    
