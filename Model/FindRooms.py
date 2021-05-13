from tkinter import *
from View import main

import sqlite3

con = sqlite3.Connection('/Controller/hm_proj.db')
cur = con.cursor()


class FindRooms():
    def findrooms(self,nb,ac,tv,wifi):
        cur.execute(
            'select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',
            ((nb.get()), ac.get(), tv.get(), wifi.get()))
        return cur.fetchall()
        # print (x)

