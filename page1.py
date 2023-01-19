from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d'%(w,h))


img=PhotoImage(file='C:\\Users\\AYUSH SINGH\\OneDrive\\Desktop\\images_for_project\\Bus_for_project.png')

Label(root,text="ONLINE BUS BOOKING SYSTEM ",font=('arial',20,'bold'),fg='red',bg='light blue').grid(row=3,column=4,padx=30)

Label(root,image=img).grid(row=2,column=4,padx=w/2.5,pady=w//100)


Label(root,text="Name: AYUSH SINGH",font=('arial',10,'bold'),fg='blue').grid(row=4,column=4,padx=30,pady=20)
Label(root,text="ENR : 211B085",font=('arial',10,'bold'),fg='blue').grid(row=5,column=4,padx=30,pady=10)
Label(root,text="Mob : 66474747747 ",font=('arial',10,'bold'),fg='blue').grid(row=6,column=4,padx=10,pady=10)

Label(root,text="SUBMITTED TO : teacher's name ",font=('arial',15,'bold'),fg='red',bg='light blue').grid(row=7,column=4,padx=10,pady=40)
Label(root,text="Project based learning",font=('arial',15,'bold'),fg='red',bg='light blue').grid(row=8,column=4,padx=50)




root.mainloop()
