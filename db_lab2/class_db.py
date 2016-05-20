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
    def ShowAllInfo(self):
        con = None
        rows = []

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT EmployeeInfo.employee_id, EmployeeInfo.employee_name, EmployeeInfo.date_of_birthday, EmployeeInfo.family, WorkPlace.position, WorkPlace.salary, WorkPlace.comp_auto, WorkPlace.start_of_working, Companies.company_name "
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

    @classmethod
    def ShowTableCompanies(self):
        con = None
        rows = []

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM Companies;")

            rows = cur.fetchall()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    @classmethod
    def ShowTableEmployeeInfo(self):
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
    def ShowTableWorkPlace(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM WorkPlace;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    @classmethod
    def ShowTableVisiting(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM Visiting;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    @classmethod
    def Accounting(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT Visiting.visit_id, Visiting.employee_id, EmployeeInfo.employee_name, Visiting.visit_date "
                        "FROM Visiting JOIN EmployeeInfo ON Visiting.employee_id=EmployeeInfo.employee_id;")

            rows = cur.fetchall()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    @classmethod
    def AddVisiting(self, request):
        con = None

        print request["date"]

        inserted_date = str(request["date"])
        inserted_id = str(request["employee_id"])

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("""INSERT INTO Visiting(employee_id, visit_date) VALUES (%s, %s);""", (inserted_id, inserted_date))
            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()

#MyDataDase.ShowEmployeeInfo()
# select Visiting.visit_id, Visiting.employee_id, EmployeeInfo.employee_name, Visiting.date from Visiting join EmployeeInfo on Visiting.employee_id=EmployeeInfo.employee_id;

