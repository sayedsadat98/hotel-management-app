from Controller import HomeController
import sqlite3

con = sqlite3.Connection('C:\XXXXFILES\SEM11\CSE470\Project\Hotel Management App\Model\Database\hm_proj.db')
cur = con.cursor()
class PaymentData():

    cur.execute(
        "create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")
    cur.execute(
        "create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
    con.commit()
    # cur.execute("alter table paymentsf add totalamt varchar")
    def checkPayment(self,idd):
        cur.execute("select * from payments where id = ?", (idd,))
        x = cur.fetchall()
        return x
    def duration(self,idd):
        cur.execute("select day,month,year,time,totalamt,r_n from paymentsf where id = ?", (idd,))
        return cur.fetchone()

    def priceOfRooms(self,roomn):
        cur.execute("select price from roomd where rn = (?)", (roomn.get(),))
        rp = cur.fetchone()

    def paymentValue(self):
        cur.execute("select id from paymentsf order by id desc")
        return cur.fetchone()



