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
fr3=Frame(root)
fr3.grid(row=2,column=4)
Label(fr3,text='BUS TICKET',font=('arial',15,'bold'),fg='green',bg='light green').grid(padx=w//3)

fr4=Frame(root,bd=5,relief="groove",bg="light green",height=400,width=500)
fr4.grid(row=6,column=3,columnspan=5,pady=10,padx=w//6)


showinfo("SEAT BOOKING","SEAT BOOKED")


def on_closing():
    
    if askyesnocancel("Quit", "for closing click YES \n click NO for mainmenu"):
        
        showinfo("INFO","THANKYOU FOR USING PYTHON BUS SERVICE")
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
