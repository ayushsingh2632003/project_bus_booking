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

Label(fr,text="ADD BUS OPERATOR DETAILS ",font=('arial',15,'bold'),fg='blue',bg='WHITE').grid(row=2,column=2,padx=w//2.7)

fr9=Frame(root)
fr9.grid(row=6,column=1,pady=50,padx=w//17)

#data type of inputs
operator_id,name,address,phone,email=StringVar(),StringVar(),StringVar(),StringVar(),StringVar()


Label(fr9,text="OPERATOR ID ",font=('arial',15,'bold')).grid(row=6,column=1)
operator_id=Entry(fr9)
operator_id.grid(row=6,column=2,padx=10)

Label(fr9,text="NAME ",font=('arial',15,'bold')).grid(row=6,column=3)
name=Entry(fr9)
name.grid(row=6,column=4,padx=10)



Label(fr9,text="ADDRESS",font=('arial',15,'bold')).grid(row=6,column=5)
address=Entry(fr9)
address.grid(row=6,column=6,padx=10)

Label(fr9,text="Phone ",font=('arial',15,'bold')).grid(row=6,column=7)
phone=Entry(fr9)
phone.grid(row=6,column=8,padx=10)

Label(fr9,text="EMAIL",font=('arial',15,'bold')).grid(row=6,column=9)
email=Entry(fr9)
email.grid(row=6,column=10,padx=10)

def add_opr():
    if len(operator_id.get())!=0 or len(name.get())!=0 or len(address.get())!=0 or len(phone.get())!=0 or len(email.get())!=0:
        y=(operator_id.get(),name.get(),address.get(),phone.get(),email.get())
        query=('insert into operator(operator_id ,name,address,phone,email) values(?,?,?,?,?)')
        cur.execute(query,y)
        con.commit()
        
        
        showinfo("add operator","operator added successfully")
        cur.execute('select * from operator')
        result=cur.fetchall()
        print(result)
    else:
        showerror("value missing","all fields must be filled")
    Label(fr9,text="check info : "+operator_id.get()+name.get()+address.get()+phone.get()+email.get(),font=("arial",15,'bold'),fg='blue').grid(row=7,column=0,pady=30,padx=10,columnspan=12)
    showinfo("notice","OPERATOR RECORD ADDED")


def edit():
    if len(operator_id.get())!=0 or len(name.get())!=0 or len(address.get())!=0 or len(phone.get())!=0 or len(email.get())!=0:
        y=(operator_id.get())
        query='select * from operator where operator_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            
            showinfo("found!! ",'record found and edited')
            y=(name.get(),address.get(),phone.get(),email.get(),operator_id.get(),)
            query='update operator set  Name=?,address=?,phone=?,email=? where operator_id=?'
            cur.execute(query,y)
            con.commit()
            result=cur.fetchall()
            print(result)
        else:
            showerror("oops!!","no record found")
        print(res)
        showinfo("operator edit","operator record edited successfully")
    else:
        showerror("value missing","all fields must be filled")
        
    con.commit()
    
        
    





    

    Label(fr9,text="check info : "+operator_id.get()+name.get()+address.get()+phone.get()+email.get(),font=("arial",15,'bold'),fg='blue').grid(row=7,column=0,pady=30,padx=10,columnspan=12)
    showinfo("notice","edited successfully")



    
def home():
    root.destroy()
    import page2_
    
add_button=Button(fr9,text="ADD",command=add_opr,font=('arial',15,'bold'))
add_button.grid(row=6,column=11,padx=10)

edit_button=Button(fr9,text="EDIT",command=edit,font=('arial',15,'bold'))
edit_button.grid(row=6,column=12,padx=10)

img_home=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\Desktop\\images_for_project\\home.png')
Button(fr,image=img_home,command=home).grid(row=3,column=2,columnspan=10)


root.mainloop()

    

