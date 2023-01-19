from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))


img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,padx=w//2.7,columnspan=12)

def page_3():
    root.destroy()
    import page3
def page_5():
    root.destroy()
    import page5

Label(root,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=1,column=2,padx=50,pady=35,columnspan=10)
Button(root,text="Seat Booking",command=page_3,width=11,height=2,font=("arial",10,"bold"),bd=4,fg="black",bg="red").grid(row=2,column=5,padx=30,pady=15)
root.bind('<KeyPress>',page_3)
Button(root,text="Checked Booked Seat",command=page_5,width=20,height=2,font=("arial",10,"bold"),bd=4,fg="black",bg="yellow").grid(row=2,column=6,padx=15)
root.bind('<KeyPress>',page_5)

Button(root,text="Add bus details ",command='root.bell',width=15,height=2,font=("arial",10,"bold"),bd=4,fg="black",bg="light green").grid(row=2,column=7,padx=10)
Label(root,text="For admin only",font=('arial',10,'italic'),fg="red").grid(row=3,column=7,pady=10)

root.mainloop()
