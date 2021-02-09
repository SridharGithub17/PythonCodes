#!/bin/usr/python
"""Note:
    This is the python program to maintain a contact list
    #Version1: Command Based
    #Version2: GUI Based for Desktop compatible 
    #Version3: GUI Based for Mobile compatible
"""
#Version1
import sqlite3
from sqlite3 import Error

def checkContact(conObj, Contact):
    cur = conObj.cursor()
    cur.execute("SELECT * FROM CONTACTS WHERE PHONE_NUMBER LIKE ?", (Contact,))
    rows = cur.fetchall()
    flag ='N'
    if rows:
        print("Entered Contact details Exist in the database")
        flag = input("Do you want to update/delete  U/D???")
        if flag.upper() == 'U':
            print("Enter New details to update :")
            enterContactDetails(conObj,flag,Contact)
        elif flag.upper() =='D':
            return flag
        else:
            for row in rows:
                    print("FirstName :", row[1])
                    print("MiddleName :", row[2])
                    print("LastName :", row[3])
                    print("ContactType :", row[4])
                    print("Number :", row[5])
                    print("Email :", row[6])
                    print("Note :", row[7])

    else:
        print("Entered Contact Not Exist in the database")
        print("Please Enter contact details  :")
        enterContactDetails(conObj, flag, Contact)

def enterContactDetails(conObj, flag, Contact ):
    cur = conObj.cursor()
    print(flag,flag.upper(), Contact)
    if flag.upper() =='U': 
        cur.execute("SELECT DISTINCT SEQ_NO FROM CONTACTS WHERE PHONE_NUMBER LIKE ?",(Contact,))
        seqNo =  cur.fetchone()
        print(seqNo)       
        #Update existing
        firstName = input("First Name  : ")
        MiddleName = input("Middle Name : ")
        lastName = input("Last Name : ")
        contactType = input("Contact Type : ")
        phoneNum = input("Contact Number : ")
        emailId = input("Email Id : ")
        desc = input("Note : ")
        cur.execute("UPDATE CONTACTS SET FIRST_NAME=?,MIDDLE_NAME=?,LAST_NAME=?,CONTACT_TYPE=?,\
                     PHONE_NUMBER=?,EMAIL=?,DESC=? WHERE SEQ_NO = ?" ,(firstName, MiddleName, lastName, contactType, phoneNum, 
                                                                       emailId,desc,int(str(seqNo[0]))))
    else:
        #Insert new
        cur.execute("SELECT MAX(SEQ_NO) FROM CONTACTS")
        maxRow =  cur.fetchone()
        firstName = input("First Name  : ")
        MiddleName = input("Middle Name : ")
        lastName = input("Last Name : ")
        contactType = input("Contact Type : ")
        phoneNum = input("Contact Number : ")
        emailId = input("Email Id : ")
        desc = input("Note : ")
        print( "Details: ", str(int(str(maxRow[0]))+1) , firstName , MiddleName ,  lastName, contactType,phoneNum, emailId, desc)
        cur.execute("INSERT INTO CONTACTS VALUES(?,?,?,?,?,?,?,?)",
                    (str(int(str(maxRow[0]))+1) , firstName , MiddleName ,  lastName, contactType,phoneNum, emailId, desc))
    cur.execute("COMMIT")

def connectDB(dbFile):
    conn = None
    try:
        conn =  sqlite3.connect(dbFile)
        print("Database Version: " ,sqlite3.version)        
        print("Connecton Successful")
        return conn
        
    except Error as e:
        print(e)
    # finally:
    #     if conn:
   #         conn.close()    
def closeConnect(conn):
    if conn:
        conn.close()
        print("Database connection closed")

def listContacts(conObj):
    cur = conObj.cursor()
    cur.execute("SELECT * FROM CONTACTS ;")
    rows = cur.fetchall()
    for row in rows:
                    print("FirstName :{0}, MiddleName : {1},LastName :{2}, ContactType :{3}, Number :{4}, Email :{5},Note :{6}".
                    format( row[1], row[2],row[3],row[4],row[5],row[6],row[7]))

def checkDuplicates(conObj):
    cur = conObj.cursor()
    cur.execute("SELECT * FROM CONTACTS GROUP BY PHONE_NUMBER HAVING COUNT(1)>1")
    rows = cur.fetchall()
    if rows:
        flag = input("There are duplicates in the contact list \n,\
                      Do you want to delete these duplciates Y/N: ")
        if flag.upper() == 'Y':
            cur.executescript("""DROP TABLE IF EXISTS T_TABLE ;
                            CREATE TABLE T_TABLE AS 
                            SELECT *  FROM CONTACTS GROUP BY TRIM(PHONE_NUMBER) HAVING COUNT(*) >= 1;
                            DROP TABLE IF EXIST _CONTACTS ;
                            ALTER TABLE CONTACTS RENAME TO _CONTACTS;
                            ALTER TABLE T_TABLE RENAME TO CONTACTS; """)
            print("Duplicates have been removed")
        else:
            print("You selected to keep duplicates...")
    else:
        print("There are no duplicates in the table :)")

    
def removeDuplicates(conObj):
    checkDuplicates(conObj)

def deleteContact(conObj):
    contact = input("Enter contact to delete : ")
    flag = checkContact(conObj, contact)
    cur = conObj.cursor()
    cur.execute("SELECT DISTINCT SEQ_NO FROM CONTACTS WHERE PHONE_NUMBER LIKE ?",(contact,))
    seqNo =  cur.fetchone()
    print( seqNo, str(seqNo[0]) )
    cur.execute("DELETE FROM CONTACTS WHERE SEQ_NO = ?",( int(str(seqNo[0])),))
    cur.execute("COMMIT")
    print("Given contact has been deleted ....")

def main():
    print("Project Contact List for Individual ")
    #Connect Contacts Database
    conObj = connectDB(r"C:\SQLLite\Databases\COLUMBUS.db")
    print("##############################################################################\n")
    print( "0: List All Contacts \n"
           "1: Insert New Contacts \n"
           "2: Update Existing Contacts \n"
           "3: Remove Duplicate Contacts\n"
           "4: Delete Existing Contacts"  )
    print("###############################################################################\n")

    start = 'Y'
    while start:
        operationType = int(input ("Please Enter the type of Operation you want to perform:  "))
        if operationType in (1,2):
            print("Enter contact number to check if contact exit or not with name or contact number")
            contactDetails = input("Enter Phone/Name to check if exist:  ")
            checkContact(conObj, contactDetails)
        elif operationType == 0:
            listContacts(conObj)
        elif operationType == 3:
            removeDuplicates(conObj)
        elif operationType == 4:
            deleteContact(conObj)
        start = input("Do you want to make any other operation Y/N? ")
        if start.upper() == 'N':
            input("Press enter to exit")
            exit("Exiting the application..")
        else:
            continue
    #Close Database Connection
    closeConnect(conObj)


if __name__ == "__main__":
    main()