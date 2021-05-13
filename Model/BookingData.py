from Controller import HomeController
import sqlite3

con = sqlite3.Connection('C:\XXXXFILES\SEM11\CSE470\Project\Hotel Management App\Model\Database\hm_proj.db')
cur = con.cursor()


class BookingData():

    def roomStatus(self,roomn):
        cur.execute("select rstatus from roomd where rn = ?", (roomn.get(),))
        return cur.fetchone()

    def sendPrice(self,roomn):
        cur.execute("select price from roomd where rn = (?)", (roomn.get(),))
        return cur.fetchone()