import os
import csv
def addAccessories():
    print ("Add a new Accessories Record")
    print("================================")
    f=open('Accessories.csv', 'a', newline='')
    s=csv.writer (f)
    Accessoriesid=int(input('Enter Shop Accessories id='))
    Accessoriesname=input ('Enter Shop Accessories name=')
    AccessoriesDOP=input ('Enter Shop Accessories DOP=')
    price=float(input('Enter price='))
    Quantity=float(input('Enter Number of Accessories='))
    rec=[Accessoriesid, Accessoriesname, AccessoriesDOP , price, Quantity]
    s.writerow(rec)
    f.close()
    print ("Accessories Record Saved")
    input("Press any key to continue..")

def modifyAccessories():
    print ("Modify Accessories Record")
    print("======================")
    f=open('Accessories.csv', 'r', newline='\r\n')
    f1=open('temp.csv', 'w', newline='\r\n')
    f1=open('temp.csv', 'a', newline='\r\n')
    r=input ('Enter Accessoriesid whose record you want to modify=')
    s=csv.reader (f)
    s1=csv.writer (f1)
    for rec in s:
        if rec[0]==r:
            print("--------------------------------")
            print("Accessories id=", rec[0])
            print("Accessories Name=", rec[1])
            print("DOP=", rec[2])
            print("Price=", rec[3])
            print("Number of Accessories=", rec[4])
            print("---------------------------------")

            choice=input ("Do you want to modify this Accessories Record (y/n)=")
            if choice=='y' or choice=='Y':
                Accessoriesid=int(input('Enter new Accessories id='))
                Accessoriesname=input ('Enter new Accessories name=')
                AccessoriesDOP=input ('Enter new author name=')
                price=float (input('Enter new price='))
                noofAccessories=float (input('Enter new number of Accessories='))
                rec [Accessoriesid, Accessoriesname, AccessoriesDOP, price, noofAccessories]
                s1.writerow(rec)
                print ("Accessories Record Modified")
            else:
                s1.writerow(rec)
        else:
                s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("Accessories.csv")
    os.rename("temp.csv", "Accessories.csv")

    input ("Press any key to continue..")

def deleteAccessories():
    f=open ('Accessories.csv', 'r', newline='\r\n')
    fl=open('temp.csv', 'w', newline='\r\n')
    f1=open('temp.csv', 'a', newline='\r\n')
    r=input ('Enter Accessoriesid whose record you want to delete')
    s=csv.reader (f)
    s1=csv.writer (fl)
    for rec in s:
        if rec[0]==r:
            print("--------------------------------")
            print("Accessories id=", rec[0])
            print("Accessories Name=", rec[1])
            print("DOP=", rec[2])
            print("Price=", rec[3])
            print("Number of Accessories=", rec[4])
            print("---------------------------------")

            choice=input ("Do you want to delete this Accessories Record (y/n)=")
            if choice=='y' or choice=='Y':
                pass
                print ("Accessories Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("Accessories.csv")
    os.rename ("temp.csv", "Accessories.csv")

    input ("Press any key to continue..")

def searchAccessories():
    print("Search a Accessories Record")
    print("===========================")
    f=open('Accessories.csv', 'r',newline='\r\n') #Remove new line character from output
    r=input('Enter Accessoriesid you want to search')
    s=csv.reader (f)
    for rec in s:
        if rec[0]==r:
            print("--------------------------------")
            print("Accessories id=", rec[0])
            print("Accessories Name=", rec[1])
            print("DOP=", rec[2])
            print("Price=", rec[3])
            print("Number of Accessories=", rec[4])
            print("---------------------------------")
    f.close()
    input ("Press any key to continue..")

def listallAccessories() :
    print ("List of All Accessories")
    print ("=======================")
    f=open ('Accessories.csv', 'r', newline='\r\n') #Remove new line character from output
    s=csv.reader (f)
    i=1
    for rec in s:
        print (rec[0], end="\t\t")
        print (rec[1], end="\t\t")
        print (rec[2], end="\t\t")
        print (rec[3], end="\t\t")
        print (rec[4])
        i+=1
    f.close()
    print("----------------------------")
    input("Press any key to continue..")

def mainmenu ():
    choice=0
    while choice!=6:
        print("\n")
        print("|-----------------------------------|")
        print("|   MOBILE SHOP Management System   |")
        print("|-----------------------------------|")
        print('\n')
        print("########################")
        print("         Main Menu")
        print("########################")
        print("1. Add a new Accessories Record")
        print("2. Modify Existing Accessories Record")
        print("3. Delete Existing Accessories Record")
        print("4. Search a Accessories")
        print("5. List all Accessories")
        print("6. Exit")
        print("-----------------------------------")
        choice=int(input('Enter Your Choice'))
        if choice==1:
            addAccessories()
        elif choice==2:
            modifyAccessories()
        elif choice==3:
            deleteAccessories()
        elif choice==4:
            searchAccessories ()
        elif choice==5:
            listallAccessories ()
        elif choice==6:
            print ("Software Terminated.......")
            break
mainmenu()
    
        
