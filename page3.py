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

#total seat variable
nos_var=IntVar()

fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)


img_bus=PhotoImage(file='.\\Bus_for_project.png')
Label(fr,image=img_bus).grid(row=0,column=2,padx=w//2.5,columnspan=12)

Label(fr,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=25,columnspan=12)
Label(fr,text="Enter Journey Details ",font=('arial',10,'bold'),fg='green',bg='light green').grid(row=2,column=2,padx=50,columnspan=12)


Label(fr,text="TO",font=('arial',15,'bold')).grid(row=4,column=4)
to_input=StringVar()
to_input=Entry(fr)
to_input.grid(row=4,column=5)



Label(fr,text="FROM",font=('arial',15,'bold')).grid(row=4,column=6)
from_input=StringVar()
from_input=Entry(fr)
from_input.grid(row=4,column=7,pady=10)

Label(fr,text="JOURNEY DATE",font=('arial',15,'bold')).grid(row=4,column=8,pady=20)
Label(fr,text="YYYY-MM-DD  format",font=("arial",7,'bold')).place(x=920,y=350)

date_input=StringVar()
date_input=Entry(fr)
date_input.grid(row=4,column=9,pady=10)

from_list=["agra","guna","delhi","indore"]
to_list=["guna","agra","indore","delhi"]

def click1():
    if len(to_input.get())!=0 or len(from_input.get())!=0 or len(date_input.get())!=0:
        y=(date_input.get())
        query='select Name,type,seatavaible,fare from operator,bus,capacity ,runs  where date=? bus.bus_id=runs.bus_id and operator.operator_id=bus.operator_id'
        ans=cur.execute(query,y)
        
        
        
        
        
        Label(fr,text="SELECT BUS",font=("arial",10,"bold"),fg="red").grid(row=5,column=5)
        Label(fr,text="OPERATOR",font=("arial",10,"bold"),fg="red").grid(row=5,column=6)
        Label(fr,text="BUS TYPE",font=("arial",10,"bold"),fg="red").grid(row=5,column=7)
        Label(fr,text="AVAILABLE/CAPACITY",font=("arial",10,"bold"),fg="red").grid(row=5,column=8)
        Label(fr,text="FARE",font=("arial",10,"bold"),fg="red").grid(row=5,column=9)
        ptb_but=Button(fr,text="PROCEED TO BOOK",command=click2,height=1,font=('arial',15,'bold'),bg='light green',fg='black')
        ptb_but.grid(row=6,column=10,padx=75,pady=40)

    else:
    
            showerror("error","all fields are to be filled")
        

      


    
        



def confirm_booking():

    askyesno("booking"," YOUR TOTAL FARE IS OF RS. 3000")
   
def click2():
    fill_pas_det=Label(fr,text="FILL PASSENGER'S DETAILS TO BOOK THE BUS TICKET",font=('arial',15,'bold'),fg='red',bg='light blue')
    fill_pas_det.grid(row=8,column=3,padx=w//5,columnspan=20,pady=20)

    
    fr2=Frame(root)
    fr2.grid(row=10,column=3,pady=20)


    Label(fr2,text="NAME",font=('arial',10,'bold')).grid(row=9,column=7,padx=10)
    Entry(fr2).grid(row=9,column=8,padx=10,pady=10)

    Label(fr2,text="GENDER ",font=('arial',10,'bold')).grid(row=9,column=9,padx=10)


    gen_type=StringVar()
    gen_type.set("select gender type")
    opt=['MALE','FEMALE','others']

    d_menu=OptionMenu(fr2,gen_type,*opt).grid(row=9,column=10,padx=30)

    
    Label(fr2,text="NO. OF SEATS ",font=('arial',10,'bold')).grid(row=9,column=11,padx=10)
    input_nos_var=Entry(fr2,textvariable=nos_var,width=10)
    input_nos_var.grid(row=9,column=12,pady=10)

    Label(fr2,text="MOBILE",font=('arial',10,'bold')).grid(row=9,column=13,padx=15)
    Entry(fr2).grid(row=9,column=14,pady=10)
    Label(fr2,text="AGE",font=('arial',10,'bold')).grid(row=9,column=15,padx=15)
    Entry(fr2,width=10).grid(row=9,column=16,pady=10)
    book_seat_button=Button(fr2,text="BOOK  SEAT",command=confirm_booking,height=1,font=('arial',15,'bold'),bg='light green',fg='black')

    book_seat_button.grid(row=9,column=17,pady=10,padx=20)
    
show_bus_but=Button(fr,text="SHOW BUSES",command=click1,height=1,font=('arial',15,'bold'),bg='light green',fg='black')
root.bind('<KeyPress>',click1)
show_bus_but.grid(row=4,column=10,pady=20)

def home():
    root.destroy()
    import page2_





img_home=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\Desktop\\images_for_project\\home.png')
Button(fr,image=img_home,command=home).grid(row=4,column=11,pady=20)
root.mainloop()

