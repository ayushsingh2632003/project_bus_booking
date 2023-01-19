from tkinter import *
from tkinter.messagebox import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)


img_bus=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\\Desktop\\images_for_project\\Bus_for_project.png')
Label(fr,image=img_bus).grid(row=0,column=2,padx=w//2.5,columnspan=12)

Label(fr,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=25,columnspan=12)

Label(fr,text="ADD NEW DETAILS TO DATABASE ",font=('arial',15,'bold'),fg='white',bg='black').grid(row=2,column=2,padx=w//2.7)


fr8=Frame(root)
fr8.grid(row=4,column=4,pady=50)

new_opr_but=Button(fr8,text="NEW OPERATOR",font=('arial',20,'bold'),fg='BLUE',bg='light green')
new_opr_but.grid(row=4,column=1,padx=30,pady=30)

new_bus=Button(fr8,text="NEW BUS ",font=('arial',20,'bold'),fg='BLUE',bg='light green')
new_bus.grid(row=4,column=3)

new_route=Button(fr8,text="NEW ROUTE ",font=('arial',20,'bold'),fg='BLUE',bg='light green')
new_route.grid(row=4,column=4,padx=30)

new_run=Button(fr8,text="NEW RUN ",font=('arial',20,'bold'),fg='BLUE',bg='light green')
new_run.grid(row=4,column=5,padx=10)
