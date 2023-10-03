import mysql.connector

def clear():
    for _ in range(65):
         print()

# ADD RECORD FUNCTIONS

def add_mobile():
    conn = mysql.connector.connect(
        host='localhost', database ='mobilestore', user ='root', password='123456'
)
    cursor = conn.cursor()
    mobile_id  = input('Enter Mobile ID:')
    comp_name  = input('Enter Company Name: ')
    quantity  = input('Enter quantity:')
    mfg_date  = input('Enter Mfg date:')
    price = input('Enter price')
    sql = 'insert into mobile(mobile_id,comp_name,quantity,mfg_date,price) values (%s,%s,%s,%s,%s)'
    Mobile_details=(mobile_id,comp_name,quantity,mfg_date,price)
    cursor.execute(sql,Mobile_details)
    conn.commit()
    conn.close()
    print("\n\nNEW Mobile ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')


def add_customer():
    conn = mysql.connector.connect(
        host = 'localhost', database ='mobilestore', user = 'root', password='123456')
    cursor = conn.cursor()
    cust_id  = input('Enter customer ID:')
    cust_name = input('Enter Customer Name: ')
    cust_address  = input('Enter Customer Address:')
    cust_age  = input('Enter Customer age : ')
    cust_phoneno = input('Enter Customer Phone No. :')
    sql = 'insert into customer(cust_id,cust_name,cust_address,cust_age,cust_phoneno) values (%s,%s,%s,%s,%s)'
    customer_details=(cust_id,cust_name,cust_address,cust_age,cust_phoneno)
    cursor.execute(sql,customer_details)
    conn.commit()
    conn.close()
    print("\n\nNEW CUSTOMER RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')

def add_bill_receipt():
    conn = mysql.connector.connect(
        host = 'localhost', database ='mobilestore', user = 'root', password='123456')
    cursor = conn.cursor()
    cust_id = input('Enter customer id:')
    cust_name = input('Enter Customer name: ')
    mobile_id = input('Enter mobile id :')
    total_amtpaid = input('Enter total amt paid:')
    sql = 'insert into billreceipt(cust_id,cust_name,mobile_id,total_amtpaid) values (%s,%s,%s,%s)'
    bill_receipt_details=(cust_id,cust_name,mobile_id,total_amtpaid)
    cursor.execute(sql,bill_receipt_details)
    conn.commit()
    conn.close()
    print("\n\nNEW bill receipt RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')

def add_employee():
    conn = mysql.connector.connect(
        host = 'localhost', database ='mobilestore', user = 'root', password='123456')
    cursor = conn.cursor()
    empl_id = input('Enter Employee ID :')
    empl_name  = input('Enter Employee Name: ')
    empl_address  = input('Enter employee address  :')
    empl_phoneno  = input('Enter Employee Phone no. :')
    date_of_joining = input('Enter Date of joining :')
    sql = 'insert into empl(empl_id,empl_name,empl_address,empl_phoneno,date_of_joining) values (%s,%s,%s,%s,%s)'
    Employee_details=(empl_id,empl_name,empl_address,empl_phoneno,date_of_joining)
    cursor.execute(sql,Employee_details)
    conn.commit()
    conn.close()
    print("\n\nNEW employee RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')



# MODIFY FUNCTIONS

def modify_mobile():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Mobile Details Screen ')
    print('-'*120)
    print('\n1. Mobile ID')
    print('\n2. Company Name')
    print('\n3. Quantity')
    print('\n4. MFG date')
    print('\n5. Price')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'mobile_id'
    if choice == 2:
        field = 'comp_name'
    if choice == 3:
        field = 'quantity'
    if choice == 4:
        field = 'mfg_date'
    if choice == 5:
        field = 'price'
    mobile_id = input('Enter mobile ID :')
    value = input('Enter new value :')
    if field == 'price':
        sql = 'update mobile set ' + field + ' = '+value+' where mobile_id = '+mobile_id+';'
    else:
        sql = 'update mobile set ' + field + ' = "'+value+'" where mobile_id = '+mobile_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nMobile details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    

def modify_customer():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Customer Details Screen ')
    print('-'*120)
    print('\n1. Customer ID')
    print('\n2. Customer Name')
    print('\n3. Customer Address')
    print('\n4. Customer Age')
    print('\n5. Customer Phone No.')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'cust_id'
    if choice == 2:
        field = 'cust_name'
    if choice == 3:
        field = 'cust_address'
    if choice == 4:
        field = 'cust_age'
    if choice == 5:
        field = 'cust_phoneno'
    cust_id = input('Enter Customer ID :')
    value = input('Enter new value :')
    sql = 'update customer set ' + field + ' = "'+value+'" where cust_id = '+cust_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nCustomer details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    

def modify_billreceipt():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Bill receipt Details Screen ')
    print('-'*120)
    print('\n1. Customer ID ')
    print('\n2. Customer Name ')
    print('\n3. Mobile ID')
    print('\n4. Total amt paid')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'cust_id'
    if choice == 2:
        field = 'cust_name'
    if choice == 3:
        field = 'mobile_id'
    if choice == 4:
        field = 'total_amtpaid'
    cust_id = input('Enter Customer ID :')
    value = input('Enter new value :')
    sql = 'update billreceipt set ' + field + ' = "'+value+'" where iss_id = '+cust_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nBill receipt details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

    
def modify_employee():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Employee Details Screen ')
    print('-'*120)
    print('\n1. Employee ID')
    print('\n2. Employee Name')
    print('\n3. Employee Address')
    print('\n4. Employee Phone No.')
    print('\n5. Date of Joining')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'empl_id'
    if choice == 2:
        field = 'empl_name'
    if choice == 3:
        field = 'empl_address'
    if choice == 4:
        field = 'empl_phoneno'
    if choice == 5:
        field = 'date_of_joining'
    empl_id = input('Enter Employee Id :')
    value = input('Enter new value :')
    sql = 'update employee set ' + field + ' = "'+value+'" where empl_id = '+empl_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nEmployee details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    
# DELETE FUNCTION

def delete_mobile():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Delete From MOBILE Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Mobile ID:')
    sql = 'delete from mobile where mobile_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nDeleted Record.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def delete_customer():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Delete from CUSTOMER Details Screen ')
    print('-'*120)
    value = input('Enter Customer ID:')
    sql = 'delete from customer where cust_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nDeleted Record.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

    
def delete_billreceipt():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Delete From Bill Receipt Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Customer ID:')
    sql = 'delete from billreceipt where cust_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nRecord Deleted.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def delete_employee():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Delete From EMPLOYEE Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Employee ID :')
    sql = 'delete from empl where empl_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nRecord Deleted.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

# Show Record

def show_records():
 conn = mysql.connector.connect(
    host='localhost', database='mobilestore', user='root', password='123456')
 cursor = conn.cursor()
 clear()
 print('Show Records')
 print('-'*120)
 print('\n1. Show Mobile')
 print('\n2. Show Customer')
 print('\n3. Show Bill Receipts')
 print('\n4. Show Employees')
 print('\n\n')
 choice = int(input('Enter your choice :'))
 field = ''
 if choice == 1:
        field = 'mobile'
 if choice == 2:
        field = 'customer'
 if choice == 3:
        field = 'billreceipt'
 if choice == 4:
        field = 'empl'
 sql = 'select * from ' +field+';'
 cursor.execute(sql)
 print(cursor.fetchall())
 wait = input('\n\n\n Press any key to continue....')
    
# MENU FUNCTION

def add_menu_screen():
    while True:
      clear()
      print("\n1.  Add MOBILE")
      print('\n2.  Add CUSTOMER')
      print('\n3.  Add BILL RECEIPT')
      print('\n4.  Add EMPLOYEE')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_mobile()
      if choice == 2:
        add_customer()
      if choice == 3:
        add_bill_receipt()
      if choice == 4:
        add_employee()
      if choice == 5:
        show_records()
      if choice == 6:
          break
        
def update_menu_screen():
    while True:
      clear()
      print("\n1.  Update MOBILE")
      print('\n2.  Update CUSTOMER')
      print('\n3.  Update BILL RECEIPT')
      print('\n4.  Update EMPLOYEE')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        modify_mobile()
      if choice == 2:
        modify_customer()
      if choice == 3:
        modify_billreceipt()
      if choice == 4:
        modify_employee()
      if choice == 5:
        show_records()
      if choice == 6:
          break
        
def delete_menu_screen():
    while True:
      clear()
      print("\n1.  Delete MOBILE")
      print('\n2.  Delete CUSTOMER')
      print('\n3.  Delete BILL RECEIPT')
      print('\n4.  Delete EMPLOYEE')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        delete_mobile()
      if choice == 2:
        delete_customer()
      if choice == 3:
        delete_billreceipt()
      if choice == 4:
        delete_employee()
      if choice == 5:
        show_records()
      if choice == 6:
          break
        
# MAIN MENU FUNCTION
def main_menu():
    while True:
      clear()
      print("******************************************************")
      print("\n")
      print("********** MOBILE SHOP MANAGEMENT SYSTEM **********")
      print("\n")
      print("******************************************************")
      print("\n1.  Add Menu")
      print('\n2.  Update Menu')
      print('\n3.  Delete Menu')
      print('\n4. Show Records')
      print('\n5. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_menu_screen()
      if choice == 2:
        update_menu_screen()
      if choice == 3:
        delete_menu_screen()
      if choice == 4:
        show_records()
      if choice == 5:
          break

if __name__ == "__main__":
    main_menu()
