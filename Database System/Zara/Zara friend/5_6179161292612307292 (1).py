import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd


def clear():
    for _ in range(65):
         print()

# ADD RECORD FUNCTIONS

def add_book():
    conn = mysql.connector.connect(
        host='localhost', database ='schooLibrary', user ='root', password='123'
)
    cursor = conn.cursor()
    book_name = input('Enter book name:')
    book_id = input('Enter book id: ')
    book_price = input('Enter book price:')
    book_publisher = input('Enter publisher name:')
    date_of_acquisition = input('Enter date of acquisition:')
    no_of_times_issued=input('Enter No. of times issued :')
    sql = 'insert into book(book_name,book_id,book_price,book_publisher,date_of_acquisition,no_of_times_issued) values (%s,%s,%s,%s,%s,%s)'
    book_details=(book_name,book_id,book_price,book_publisher,date_of_acquisition,no_of_times_issued)
    cursor.execute(sql,book_details)
    conn.commit()
    conn.close()
    print("\n\nNEW BOOK ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')


def add_issuance():
    conn = mysql.connector.connect(
        host = 'localhost', database ='schooLibrary', user = 'root', password='123')
    cursor = conn.cursor()
    std_reg_no = input('Enter student registration no.:')
    book_id = input('Enter book id: ')
    issuer_id = input('Enter issuer id:')
    date_of_issue = input('Enter issue date')
    date_of_return = input('Enter return date :')
    fine = input('Enter fine imposed :')
    sql = 'insert into issuance(std_reg_no,book_id,issuer_id,date_of_issue,date_of_return,fine) values (%s,%s,%s,%s,%s,%s)'
    issuance_details=(std_reg_no,book_id,issuer_id,date_of_issue,date_of_return,fine)
    cursor.execute(sql,issuance_details)
    conn.commit()
    conn.close()
    print("\n\nNEW ISSUANCE RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')

def add_issuer():
    conn = mysql.connector.connect(
        host = 'localhost', database ='schooLibrary', user = 'root', password='123')
    cursor = conn.cursor()
    iss_name = input('Enter issuer name.:')
    iss_id = input('Enter issuer id: ')
    iss_phone = input('Enter issuer phone no. :')
    iss_email = input('Enter issuer email:')
    sql = 'insert into issuer(iss_name,iss_id,iss_phone,iss_email) values (%s,%s,%s,%s)'
    issuer_details=(iss_name,iss_id,iss_phone,iss_email)
    cursor.execute(sql,issuer_details)
    conn.commit()
    conn.close()
    print("\n\nNEW ISSUER RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')

def add_student():
    conn = mysql.connector.connect(
        host = 'localhost', database ='schooLibrary', user = 'root', password='123')
    cursor = conn.cursor()
    std_name = input('Enter student name.:')
    std_class = input('Enter student class: ')
    std_roll_no = input('Enter student roll no. :')
    std_reg_no = input('Enter student registration no.:')
    std_phone = input('Enter student phone no.:')
    sql = 'insert into student(std_name,std_class,std_roll_no,std_reg_no,std_phone) values (%s,%s,%s,%s,%s)'
    student_details=(std_name,std_class,std_roll_no,std_reg_no,std_phone)
    cursor.execute(sql,student_details)
    conn.commit()
    conn.close()
    print("\n\nNEW STUDENT RECORD ADDED SUCCESSFULLY")
    wait = input('\n\n\PRESS ANY KEY TO CONTINUE')

# MODIFY FUNCTIONS

def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Name')
    print('\n2. Book ID')
    print('\n3. Book Price')
    print('\n4. Book Publisher Name')
    print('\n5. Date Of Acquisition')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'book_name'
    if choice == 2:
        field = 'book_id'
    if choice == 3:
        field = 'book_price'
    if choice == 4:
        field = 'book_publisher'
    if choice == 5:
        field = 'date_of_acquisition'
    if choice == 6:
        field = 'no_of_times_issued'
    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    sql = 'update book set ' + field + ' = "'+value+'" where book_id = '+book_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nBook details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    

def modify_issuance():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Modify ISSUANCE Details Screen ')
    print('-'*120)
    print('\n1. Student Registration No.')
    print('\n2. Book ID')
    print('\n3. Issuer ID')
    print('\n4. Date of Issue')
    print('\n5. Date of Return')
    print('\n6. Fine')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'std_reg_no'
    if choice == 2:
        field = 'book_id'
    if choice == 3:
        field = 'issuer_id'
    if choice == 4:
        field = 'date_of_issue'
    if choice == 5:
        field = 'date_of_return'
    if choice == 6:
        field = 'fine'
    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    sql = 'update issuance set ' + field + ' = "'+value+'" where book_id = '+book_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nIssuance details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    

def modify_issuer():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Modify ISSUANCE Details Screen ')
    print('-'*120)
    print('\n1. Issuer Name.')
    print('\n2. Issuer ID')
    print('\n3. Issuer Phone')
    print('\n4. Issuer Email')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'iss_name'
    if choice == 2:
        field = 'iss_id'
    if choice == 3:
        field = 'iss_phone'
    if choice == 4:
        field = 'iss_email'
    iss_id = input('Enter Issuer ID :')
    value = input('Enter new value :')
    sql = 'update issuer set ' + field + ' = "'+value+'" where iss_id = '+iss_id+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nIssuer details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

    
def modify_student():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Modify ISSUANCE Details Screen ')
    print('-'*120)
    print('\n1. Student Name')
    print('\n2. Student Class')
    print('\n3. Student Roll No.')
    print('\n4. Studnet Registration No.')
    print('\n5. Student Phone No.')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'std_name'
    if choice == 2:
        field = 'std_class'
    if choice == 3:
        field = 'std_roll_no'
    if choice == 4:
        field = 'std_reg_no'
    if choice == 5:
        field = 'std_phone'
    std_reg_no = input('Enter Student Registration No. :')
    value = input('Enter new value :')
    sql = 'update student set ' + field + ' = "'+value+'" where std_reg_no = '+std_reg_no+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nIssuance details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
    
# DELETE FUNCTION

def delete_book():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Delete From BOOK Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Book ID :')
    sql = 'delete from book where book_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nDeleted Record.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def delete_issuance():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Delete from ISSUANCE Details Screen ')
    print('-'*120)
    value = input('Enter book id :')
    sql = 'delete from issuance where book_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nDeleted Record.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

    
def delete_issuer():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Delete From ISSUER Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Issuer ID:')
    sql = 'delete from issuer where iss_id ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nRecord Deleted.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def delete_student():
    conn = mysql.connector.connect(
        host='localhost', database='schooLibrary', user='root', password='123')
    cursor = conn.cursor()
    clear()
    print('Delete From STUDENT Details Screen ')
    print('-'*120)
    print('\n\n')
    value = input('Enter Student Registration No. :')
    sql = 'delete from student where std_reg_no ='+value+';'
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nRecord Deleted.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

# Show Record
def show_records():
 conn = mysql.connector.connect(
    host='localhost', database='schooLibrary', user='root', password='123')
 cursor = conn.cursor()
 clear()
 print('Show Records')
 print('-'*120)
 print('\n1. Show Book')
 print('\n2. Show Issuance')
 print('\n3. Show Issuer')
 print('\n4. Show Student')
 print('\n\n')
 choice = int(input('Enter your choice :'))
 field = ''
 if choice == 1:
        field = 'book'
 if choice == 2:
        field = 'issuance'
 if choice == 3:
        field = 'issuer'
 if choice == 4:
        field = 'student'
 sql = 'select * from ' +field+';'
 cursor.execute(sql)
 print(cursor.fetchall())
 wait = input('\n\n\n Press any key to continue....')

# Data Visualization

def pandas_book():
   clear()
   print("\n\t DATA VISUALISATION\t")
   print("\n---------------------------------------\n")
   print("DISPLAYING PRICE FOR BOOKS")
   df = pd.read_csv("issued.csv")
   x = df['book_name']
   y = df['no_of_times_issued']
   plt.bar(x,y)
   plt.title('BOOK & NO. OF TIMES ISSUED')
   plt.xlabel('BOOK NAME')
   plt.ylabel('NO OF TIMES ISSUED')
   plt.show()
   wait = input('\n\n\n Press any key to continue....')

# MENU FUNCTION
def add_menu_screen():
    while True:
      clear()
      print("\n1.  Add BOOK")
      print('\n2.  Add ISSUANCE')
      print('\n3.  Add ISSUER')
      print('\n4.  Add STUDENT')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_issuance()
      if choice == 3:
        add_issuer()
      if choice == 4:
        add_student()
      if choice == 5:
        show_records()
      if choice == 6:
          break
        
def update_menu_screen():
    while True:
      clear()
      print("\n1.  Update BOOK")
      print('\n2.  Update ISSUANCE')
      print('\n3.  Update ISSUER')
      print('\n4.  Update STUDENT')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        modify_book()
      if choice == 2:
        modify_issuance()
      if choice == 3:
        modify_issuer()
      if choice == 4:
        modify_student()
      if choice == 5:
        show_records()
      if choice == 6:
          break
        
def delete_menu_screen():
    while True:
      clear()
      print("\n1.  Delete BOOK")
      print('\n2.  Delete ISSUANCE')
      print('\n3.  Delete ISSUER')
      print('\n4.  Delete STUDENT')
      print('\n5. Show Records')
      print('\n6. Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        delete_book()
      if choice == 2:
        delete_issuance()
      if choice == 3:
        delete_issuer()
      if choice == 4:
        delete_student()
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
      print("********** SCHOOL LIBRARY MANAGEMENT SYSTEM **********")
      print("\n")
      print("******************************************************")
      print("\n1.  Add Menu")
      print('\n2.  Update Menu')
      print('\n3.  Delete Menu')
      print('\n4. Show Records')
      print('\n5. Data Visualisation')
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
         pandas_book()
      if choice == 6:
         break

if __name__ == "__main__":
    main_menu()
