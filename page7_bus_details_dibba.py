from tkinter import*
from tkinter.messagebox import *

#Create the database in python
import sqlite3
con=sqlite3.Connection('Bus_Booking')
cur=con.cursor()
cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_i number,route_id number,foreign key(operator_i) references operator(operator_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(Bus_id number,date date ,seatavaible number,PRIMARY KEY(Bus_id,date))')
cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number)')


root=Tk()
root.title('Bus Details')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\\Desktop\\images_for_project\\Bus_for_project.png')
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//15)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
Label(root,text='Add Bus Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)
Label(root,text='').grid(row=3,column=0,padx=5)
Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)

Bus_id=Entry(root,font="Arial 12 bold")        # For intry Box 
Bus_id.grid(row=3,column=2,padx=0)

Label(root,text='Bus Type',font="Arial 12 bold").grid(row=3,column=3)
Bus_type=StringVar()
opt=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non-AC-Sleeper 2X1"]
Bus_type.set('Bustype')
d_menu=OptionMenu(root,Bus_type,*opt).grid(row=3,column=4)          # For intry Box
Label(root,text='Capacity',font="Arial 12 bold").grid(row=3,column=5)
Capacity=Entry(root,font="Arial 12 bold")# For intry Box
Capacity.grid(row=3,column=6,padx=0)
Label(root,text='Fare Rs',font="Arial 12 bold").grid(row=3,column=7,padx=0)
Fare=Entry(root,font="Arial 12 bold")# For intry Box
Fare.grid(row=3,column=8,padx=0)
Label(root,text='Operator ID',font="Arial 12 bold").grid(row=3,column=9,padx=0)

Operator_ID=Entry(root,font="Arial 10 bold")# For intry Box
Operator_ID.grid(row=3,column=10,padx=0)
Label(root,text='Route ID',font="Arial 12 bold").grid(row=3,column=11,padx=0)
Route_id=Entry(root,font="Arial 12 bold")# For intry Box
Route_id.grid(row=3,column=12,pady=90)
def Add_Bus():
    if len(Operator_ID.get())!=0 or len(Route_id.get())!=0 or len(Fare.get())!=0 or len(Capacity.get())!=0 or len(Bus_id.get())!=0:
        y=(Bus_id.get(),Bus_type.get(),Capacity.get(),Fare.get(),Operator_ID.get(),Route_id.get())
        query=('insert into bus(Bus_id ,type ,capacity,fare, route_id,operator_i) values(?,?,?,?,?,?)')
        cur.execute(query,y)
        con.commit()
        showinfo('Add Bus Entry','Bus Record Added')
        cur.execute('select * from bus')
        result=cur.fetchall()
        print(result)
    else:
        showerror('Value Missing','Please Enter The Values')
def Edit_Bus():
    if len(Operator_ID.get())!=0 or len(Route_id.get())!=0 or len(Fare.get())!=0 or len(Capacity.get())!=0 or len(Bus_id.get())!=0:
        y=(Bus_id.get())
        query='select * from bus where bus_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            showinfo('Found','record found')
            y=(Bus_type.get(),Capacity.get(),Fare.get(),Route_id.get(),Operator_ID.get(),Bus_id.get())
            query='update bus set type=? ,capacity=?,fare=?,route_id=?,operator_i =? where bus_id=?'
            cur.execute(query,y)
            con.commit()
            cur.execute('select * from bus')
            result=cur.fetchall()
            print(result)
        else:
            showerror('not found','error')
            
        print(res)
        showinfo('Bus Entry Edit','Bus Record Edited Successfully')
    else:
        showerror('Value Missing','Please Enter The Values')
Button(root,text="Add Bus",font="Arial 15 bold",bg="light green",command=Add_Bus).grid(row=4,column=7)    # Boutton for Show bus
Button(root,text="Edit Bus",font="Arial 15 bold",bg="light green",command=Edit_Bus).grid(row=4,column=8)
Home_img=PhotoImage(file=".\\home.png")    # For read image
Button(root,image=Home_img,bg="green").grid(row=4,column=9)       # For Display image as a Button

root.mainloop()
