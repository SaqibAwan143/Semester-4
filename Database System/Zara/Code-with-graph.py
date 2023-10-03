import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

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
    model_name  = input('Enter model Name: ')
    quantity  = input('Enter quantity:')
    mfg_date  = input('Enter Mfg date:')
    price = input('Enter price')
    sql = 'insert into mobile(mobile_id,model_name,quantity,mfg_date,price) values (%s,%s,%s,%s,%s)'
    Mobile_details=(mobile_id,model_name,quantity,mfg_date,price)
    cursor.execute(sql,Mobile_details)
    conn.commit()
    conn.close()
    print("\n\nNEW Mobile ADDED SUCCESSFULLY")
    input('\n\n\PRESS ANY KEY TO CONTINUE')


def add_customer():
    conn = mysql.connector.connect(
        host = 'localhost', database ='mobilestore', user = 'root', password='123456')
    cursor = conn.cursor()
    cust_id  = input('Enter customer ID:')
    cust_name = input('Enter Customer Name: ')
    cust_address  = input('Enter Customer Address:')
    cust_dob  = input('Enter Customer date of birth: ')
    cust_phoneno = input('Enter Customer Phone No. :')
    sql = 'insert into customer(cust_id,cust_name,cust_address,cust_dob,cust_phoneno) values (%s,%s,%s,%s,%s)'
    customer_details=(cust_id,cust_name,cust_address,cust_dob,cust_phoneno)
    cursor.execute(sql,customer_details)
    conn.commit()
    conn.close()
    print("\n\nNEW CUSTOMER RECORD ADDED SUCCESSFULLY")
    input('\n\n\PRESS ANY KEY TO CONTINUE')

def add_bill_receipt():
    conn = mysql.connector.connect(
        host = 'localhost', database ='mobilestore', user = 'root', password='123456')
    cursor = conn.cursor()
    bill_no  = input('Enter Bill no:')
    bill_date  = input('Enter Bill Date ')
    cust_id  = input('Enter Customer ID :')
    model_id  = input('Enter Model ID:')
    sql = 'insert into billreceipt(bill_no,bill_date,cust_id,model_id) values (%s,%s,%s,%s)'
    bill_receipt_details=(bill_no,bill_date,cust_id,model_id)
    cursor.execute(sql,bill_receipt_details)
    conn.commit()
    conn.close()
    print("\n\nNEW bill receipt RECORD ADDED SUCCESSFULLY")
    input('\n\n\PRESS ANY KEY TO CONTINUE')


# MODIFY FUNCTIONS

def modify_mobile():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Mobile Details Screen ')
    print('-'*120)
    print('\n1. Mobile ID')
    print('\n2. Model Name')
    print('\n3. Quantity')
    print('\n4. MFG date')
    print('\n5. Price')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'mobile_id'
    if choice == 2:
        field = 'model_name'
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
    input('\n\n\n Press any key to continue....')
    

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
    print('\n4. Customer Date of birth')
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
        field = 'cust_dob'
    if choice == 5:
        field = 'cust_phoneno'
    cust_id = input('Enter Customer ID :')
    value = input('Enter new value :')
    sql = 'update customer set ' + field + ' = "'+value+'" where cust_id = '+cust_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nCustomer details Updated.....')
    conn.close()
    input('\n\n\n Press any key to continue....')
    

def modify_billreceipt():
    conn = mysql.connector.connect(
        host='localhost', database='mobilestore', user='root', password='123456')
    cursor = conn.cursor()
    clear()
    print('Modify Bill receipt Details Screen ')
    print('-'*120)
    print('\n1. Bill No ')
    print('\n2. Bill Date ')
    print('\n3. Customer ID')
    print('\n4. Mobile ID')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'bill_no'
    if choice == 2:
        field = 'bill_date'
    if choice == 3:
        field = 'cust_id'
    if choice == 4:
        field = 'model_id'
    cust_id = input('Enter Customer ID :')
    value = input('Enter new value :')
    sql = 'update billreceipt set ' + field + ' = "'+value+'" where iss_id = '+cust_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nBill receipt details Updated.....')
    conn.close()
    input('\n\n\n Press any key to continue....')

    
    
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
    input('\n\n\n Press any key to continue....')

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
    input('\n\n\n Press any key to continue....')

    
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
    input('\n\n\n Press any key to continue....')


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
 print('\n\n')
 choice = int(input('Enter your choice :'))
 field = ''
 if choice == 1:
        field = 'mobile'
 if choice == 2:
        field = 'customer'
 if choice == 3:
        field = 'billreceipt'
 sql = 'select * from ' +field+';'
 cursor.execute(sql)
 print(cursor.fetchall())
 input('\n\n\n Press any key to continue....')

 # Data Visualization

def pandas_mobile():
   clear()
   print("\n\t DATA VISUALISATION\t")
   print("\n---------------------------------------\n")
   print("DISPLAYING PRICE FOR MOBILE")
   df = pd.read_csv('CSv Location')
   x = df['model_name']
   y = df['price']
   plt.bar(x,y)
   plt.title('MODEL NAME & PRICE')
   plt.xlabel('MODEL NAME')
   plt.ylabel('PRICE')
   plt.show()
   input('\n\n\n Press any key to continue....')
    
# MENU FUNCTION

def add_menu_screen():
    while True:
      clear()
      print("\n1.  Add MOBILE")
      print('\n2.  Add CUSTOMER')
      print('\n3.  Add BILL RECEIPT')
      print('\n4.  Show Records')
      print('\n5.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_mobile()
      if choice == 2:
        add_customer()
      if choice == 3:
        add_bill_receipt()
      if choice == 4:
        show_records()
      if choice == 5:
          break
        
def update_menu_screen():
    while True:
      clear()
      print("\n1.  Update MOBILE")
      print('\n2.  Update CUSTOMER')
      print('\n3.  Update BILL RECEIPT')
      print('\n4. Show Records')
      print('\n5. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        modify_mobile()
      if choice == 2:
        modify_customer()
      if choice == 3:
        modify_billreceipt()
      if choice == 4:
        show_records()
      if choice == 5:
          break
        
def delete_menu_screen():
    while True:
      clear()
      print("\n1.  Delete MOBILE")
      print('\n2.  Delete CUSTOMER')
      print('\n3.  Delete BILL RECEIPT')
      print('\n4. Show Records')
      print('\n5. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        delete_mobile()
      if choice == 2:
        delete_customer()
      if choice == 3:
        delete_billreceipt()
      if choice == 4:
        show_records()
      if choice == 5:
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
