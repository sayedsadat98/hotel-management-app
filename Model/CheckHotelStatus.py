import sqlite3

con = sqlite3.Connection('C:\XXXXFILES\SEM11\CSE470\Project\Hotel Management App\Model\Database\hm_proj.db')
cur = con.cursor()
class HotelStatus():

    def checkStatus(self):

        cur.execute("select * from hoteld")
        return cur.fetchall()
    def countRoom(self):
        cur.execute("select count(rn) from roomd")
        return cur.fetchone()
    def isReserved(self):
        cur.execute("select count(rn) from roomd where rstatus = 'Reserved'")
        return cur.fetchone()

