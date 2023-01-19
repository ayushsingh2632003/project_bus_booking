from tkinter import *
from tkinter.messagebox import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)


img_bus=PhotoImage(file='.\\Bus_for_project.png')
Label(fr,image=img_bus).grid(row=0,column=2,padx=w//2.5,columnspan=12)

Label(fr,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=25,columnspan=12)
fr5=Frame(root)
fr5.grid(row=2,column=4)
Label(fr5,text='CHECK YOUR BOOKING',font=('arial',15,'bold'),fg='green',bg='light green').grid(padx=w//3)


fr6=Frame(root)
fr6.grid(row=4,column=4,pady=10)

mob_no=IntVar()

Label(fr6,text="ENTER YOUR MOBILE NUMBER  ",font=('arial',15,'bold')).grid(row=4,column=3)
var_mob_no=IntVar()
input_mob_no=Entry(fr6)
input_mob_no.grid(row=4,column=5)



def check_booking():
    
    fr4=Frame(root,bd=5,relief="groove",bg="light green",height=400,width=500)
    fr4.grid(row=6,column=3,columnspan=5,pady=10,padx=w//6)


    askyesno("no booked ticked found","do you want to book bus ticket ?")


check_booking_button=Button(fr6,command=check_booking,text="CHECK BOOKING",font=('arial',15,'bold'))

check_booking_button.grid(row=4,column=6,padx=20)

root.mainloop()





