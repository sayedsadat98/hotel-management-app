from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from Controller import HomeController

import os
import sqlite3

con = sqlite3.Connection('C:\XXXXFILES\SEM11\CSE470\Project\Hotel Management App\Model\Database\hm_proj.db')
cur = con.cursor()
class RoomDetails():

    def unreserve(self,roomn):
        cur.execute("update roomd set rstatus='Unreserved' where rn = ? ", (roomn.get(),))
        HomeController.messagebox.showinfo("Successful", "Room Unreserved successfully")
        HomeController.reserve()
        con.commit()

    def findrooms(self,nb, ac, tv, wifi):
        cur.execute(
            'select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',
            ((nb.get()), ac.get(), tv.get(), wifi.get()))
        x = cur.fetchall()

    def roomDetail(self,rno):
        cur.execute("select * from roomd where rn = ?", (rno,))
        return cur.fetchall()


