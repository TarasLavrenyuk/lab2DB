import sys
import MySQLdb as mydb

class MyDataDase:

    host = 'localhost'
    db_user_name = 'root'
    password = '852456aaa'
    db_name = 'mydb'

    @classmethod
    def GetVersion(self):

        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT VERSION()")

            ver = cur.fetchone()

            print "Database version : %s " % ver

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:

            if con:
                con.close()

    @classmethod
    def ShowEmployeeInfoTable(self):

        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM EmployeeInfo;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    @classmethod
    def AllEmployees(self):

        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT EmployeeInfo.employee_id, EmployeeInfo.employee_name, WorkPlace.position, WorkPlace.salary, Companies.company_name "
                        "FROM EmployeeInfo JOIN WorkPlace ON EmployeeInfo.workplace_id=WorkPlace.workplace_id "
                        "JOIN Companies ON WorkPlace.company_id=Companies.company_id;")

            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows



#MyDataDase.ShowEmployeeInfo()