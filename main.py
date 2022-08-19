from _ast import Break

import mysql.connector
from mysql.connector import Error


def Create_Table():
    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        query = "CREATE TABLE `studentdb`.`studinfo` (`firstname` VARCHAR(100) NOT NULL , `lastname` VARCHAR(100) NOT " \
                "NULL , `email` VARCHAR(100) NOT NULL , `stud_num`VARCHAR(100) NOT NULL, `section` VARCHAR(100) " \
                "NOT NULL , PRIMARY KEY (`stud_num`)) ENGINE = InnoDB; "

        cur = con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
    except Error as error:
        print("Table Creation Failed {}".format(error))
    finally:
        if con.is_connected():
            con.close()
            print("MySQL Connection is now closed.")


def Insert_Data():
    firstname = input("Enter The Student's First Name: ")
    lastname = input("Enter The Student's Last Name: ")
    email = input("Enter Student's Email: ")
    stud_num = input("Enter Student's ID: ")
    section = input("Enter Student's Section: ")

    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        query = "INSERT INTO studinfo (firstname, lastname , email, stud_num ,section) VALUES ('" + firstname + "', '" + lastname \
                + "', '" + email + "', '" + stud_num + "', '" + section + "')"

        cur = con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
    except Error as error:
        print("Insert Data Failed {}".format(error))
    finally:
        if con.is_connected():
            con.close()
            print("MySQL Connection is now closed.")


def View_Section():
    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        section = input("Enter section that you want to see: ")
        query = "SELECT * FROM studinfo WHERE section = '" + section + "'"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchall()
        print("All Students: ", cur.rowcount)
        for row in records:
            print("Firstname: ", row[0])
            print("Lastname: ", row[1])
            print("Email: ", row[2])
            print("Student Number: ", row[3])
            print("Section: ", row[4])
            print("-------------------------")

    except Error as error:
        print("There is an error in the program".format(error))
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now closed")


def Search():
    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        sect = input("Input the student number of the student: ")
        query = "SELECT `firstname`, `lastname`, `email`, `stud_num`, `section` FROM `studinfo` WHERE stud_num = '" + sect + "'"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchall()
        print("All Students: ", cur.rowcount)
        for row in records:
            print("Firstname: ", row[0])
            print("Lastname: ", row[1])
            print("Email: ", row[2])
            print("Student Number: ", row[3])
            print("Section: ", row[4])
            print("-------------------------")

    except Error as error:
        print("There is an error in the program".format(error))
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now closed")


def View_Student():
    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        query = "SELECT * FROM studinfo"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchall()
        print("All Students: ", cur.rowcount)
        for row in records:
            print("Firstname: ", row[0])
            print("Lastname: ", row[1])
            print("Email: ", row[2])
            print("Student Number: ", row[3])
            print("Section: ", row[4])
            print("-------------------------")

    except Error as error:
        print("There is an error in the program".format(error))
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now closed")


def Edit_Data():
    try:
        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        data = input("Enter Student ID: ")
        # before update
        select_query = "SELECT * FROM studinfo WHERE stud_num = '"+data+"'"
        cur = con.cursor()
        cur.execute(select_query)
        record = cur.fetchone()
        print(record)
        # Edit Record
        enter0 = input("Enter The student's First name: ")
        enter =input("Enter The Student's Last Name: ")
        enter1 = input("Enter Student's Email: ")
        enter2 =input("Enter Student's ID: ")
        enter3 =input("Enter Student's Section: ")
        update_query = "UPDATE `studinfo` SET `firstname`='"+enter0+"',`lastname`='"+enter+"',`email`='"+enter1+"',`stud_num`='"+enter2+"',`section`='"+enter3+"' WHERE stud_num ='"+data+"'"
        cur.execute(update_query)
        con.commit()
        print("Successfully edited record!")



    except Error as error:
        print("Update Failed: {}".format(error))

    finally:
        if con.is_connected():
            con.close()
            print("MySQL Connection is now closed.")


def Delete():
    try:
        delete_student = input("Enter ID number: ")

        con = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='')
        query = "SELECT * FROM studinfo WHERE stud_num ='"+delete_student+"'"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchone()
        print("Records: ",records)


        del_query = "DELETE FROM `studinfo` WHERE stud_num = '"+delete_student+"'"
        cur.execute(del_query)
        con.commit()
        print("Record Deleted Successfully!")


    except Error as error:
        print("Error in the program {}".format(error))
    finally:
        if con.is_connected():
            con.close()
            print("MySQL Connection is now closed.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Create_Table()

while True:
    print("[1] Insert")
    print("[2] Search")
    print("[3] View Sections")
    print("[4] View Students")
    print("[5] Edit")
    print("[6] Delete")
    print("[7] Exit")

    choice = input("Please enter number: ")

    if choice == "1":
        Insert_Data()
    elif choice == "2":
        Search()
    elif choice == "3":
        View_Section()
    elif choice == "4":
        View_Student()
    elif choice == "5":
        Edit_Data()
    elif choice == "6":
        Delete()
    else:
        print("Program Exiting")
        exit()




