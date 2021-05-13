
from Model import HotelStatus
from tkinter import *
from tkinter import ttk
from Model import BookingData
from Model import PaymentData
from Model import RoomDetails
import time
import datetime
from PIL import ImageTk,Image
from Model import FindRooms
import os
import sqlite3
from tkinter import messagebox
now = datetime.datetime.now()
#----------- importing sqlite for server side operations---------------------------------------------------------------------------------

#pmethod=0

#rstatus extra column
#for i in range (1,21):
#cur.execute("update roomd set tv='Yes' where rn = ? ",(19,))


#cur.execute("drop table paymentsf")
#cur.execute("insert into hoteld values(20,11,30)")
# con.commit()
# cur.execute("select * from payments")
# con.commit()
# x=cur.fetchall()
# con.commit()
#print(x)
#-----------splash_screen------------------------------------------------------------------------------------------------------------------

	sl_frame = Frame(root,height=130,width=1080,bg='white')
	sl_frame.place(x=0,y=70+6)
	path = "images/rooms.png"
	img = ImageTk.PhotoImage(Image.open(path))
	b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180,command=rooms)
	b1.image = img
	b1.place(x=180,y=0)
	path2 = "images/hotelstatus.png"
	img1 = ImageTk.PhotoImage(Image.open(path2))
	b2 = Button(sl_frame,image=img1,text='b2',bg='white',width=180,command=hotel_status)
	b2.image = img1
	b2.place(x=0,y=0)
	path3='images/guests.png'
	img3 = ImageTk.PhotoImage(Image.open(path3))
	b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180,command=staff)
	b3.image = img3
	b3.place(x=180*4,y=0)
	path4='images/payments.png'
	img4 = ImageTk.PhotoImage(Image.open(path4))
	b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180,command = payments)
	b4.image = img4
	b4.place(x=180*3,y=0)
	path5='images/logout.png'
	img5 = ImageTk.PhotoImage(Image.open(path5))
	b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100,command=login)
	b5.image = img5
	b5.place(x=180*5,y=0)
	path6='images/Bookroom.png'
	img6 = ImageTk.PhotoImage(Image.open(path6))
	b6 = Button(sl_frame,image=img6,text='b2',bg='white',width=180,height=100,command=reserve)
	b6.image = img6
	b6.place(x=180*2,y=0)
	Label(sl_frame,text='Hotel Status',font='msserif 13',bg='white').place(x=35,y=106)
	Label(sl_frame,text='Rooms',font='msserif 13',bg='white').place(x=248,y=106)
	Label(sl_frame,text='Reserve',font='msserif 13',bg='white').place(x=417,y=106)
	Label(sl_frame,text='Contacts',font='msserif 13',bg='white').place(x=774,y=106)
	Label(sl_frame,text='Payments Info',font='msserif 13',bg='white').place(x=570,y=106)
	Label(sl_frame,text='Exit',font='msserif 13',bg='white').place(x=968,y=106)
	sl_frame.pack_propagate(False)
	#-------------------extra frame------------------------------------------------------------------------------------------------------------------
	redf = Frame(root,height=6,width=1080,bg='lightsteelblue3')
	redf.place(x=0,y=70)
	redf1 = Frame(root,height=40,width=1080,bg='lightsteelblue3')
	redf1.place(x=0,y=210)
	#-------------------------------------------------------------------------------------------------------------------------------------------------
	#hotel_status() # calling the bottom frame for default page
	# login()
	#rooms()
	#payments()
	#cur.execute("select * from roomd ")
	#x = cur.fetchall()
	#print (x) 
	reserve()
	#staff()
	datetime()
	mainloop()
def call_mainroot():
	sroot.destroy()
	mainroot()
sroot.after(3000,call_mainroot)
mainloop()