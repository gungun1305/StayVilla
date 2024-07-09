#-------------------------------------------------------------HOTEL MANAGEMENT SYSTEM---------------------------------------------------------
def pricebreakup():
    import os
    os.system('cls')
    print('''OUR PRICE BREAKUP-->
+-----------------------+-------------------+
| CHARGES PER ROOM TYPE -->  |
+-----------------------+-------------------+
 	 #| Studio --> Rs1500            |
 	 #| Double--> Rs2500            |
     	 #| King   --> Rs5000              |
     	 #| Triple --> Rs3000             |
	 #| Queen --> Rs4500            |
	 #| Quad -->  Rs4000             |
	 #| Mini Suite--> Rs10000  |
                      #| Master Suite--> Rs15000|
+--------------+------------------+---------+''')

    print('''
+-----------------------+-------------------+
| RESTAURANT MENU -->  |
+-----------------------+-------------------+
 	 #| WATER --> Rs20                |
 	 #| TEA/COFFEE--> Rs50            |
     	 #| BREAKFAST COMBO--> Rs250      |
 	 #| LUNCH COMBO--> Rs550          |
	 #| DINNER COMBO --> Rs4500       |
+--------------+------------------+---------+''')

  

    print('''
+-----------------------+-------------------+
| ENTERTAINMENT -->  |
+-----------------------+-------------------+
 	 #| GYM                    |
 	 #| SPA                    |
     	 #| BAR                    |
 	 #| CASINO                 | 
	 #| SWIMMING               |
+--------------+------------------+---------+''')
    n=input('')
#------------------------------------------------------------------GET ROOM NO.-----------------------------------------------------------------------
def Roomno():
    import os
    os.system('cls')
    print("\n\n*WELCOME TO HOTEL*\n")
    p=(input("Enter your name:"))
    n=(input("Enter your address:"))
    a=(input("Enter your check in date:"))
    b=(input("Enter your check out date:"))                                                                            
    print("We have the following rooms for you:-")
    print("1.Master Suite---->Rs15000 PN\-")
    print("2.Mini Suite---->Rs10000 PN\-")
    print("3.King---->Rs5000 PN\-")
    print("4.Queen---->Rs4500 PN\-")
    print("5.Quad---->Rs4000 PN\-")
    print("6.Triple---->Rs3000 PN\-")
    print("7.Double---->Rs2500 PN\-")
    print("8.Studio---->Rs1500 PN\-")

    x=int(input("Enter Your Choice Please->"))
    name=" "
    if(x==1):
        print("you have opted for Master Suite")
        name="Master Suit"
        s=15000*n
    elif(x==2):
        print("you have opted for Mini Suite")
        name="Mini suit"
        s=10000*n
    elif(x==3):
        print("you have opted for King")
        name="King"
        s=5000*n
    elif(x==4):
        print("you have opted for Queen")
        name="Queen"
        s=4500*n
    elif(x==5):
        print("you have opted for Quad")
        name="Quad"
        s=4000*n
    elif(x==6):
        print("you have opted for Triple")
        name="Triple"
        s=3000*n
    elif(x==7):
        print("you have opted for Double")
        name="Double"
        s=2500*n
    elif(x==8):
        print("you have opted for Studio")
        name="Studio"
        s=1500*n
    else:
        print("please choose a room")
    print("Your Room no is:")
    import  mysql.connector
    mydb=mysql.connector.connect(host ='localhost',user='root',password='1234',db='hotel_management_system')
    mycursor=mydb.cursor()
    mycursor.execute("Select Room_no, Room_type from Rooms where room_type='{}' and occupied='NO'".format(name))
    rs=mycursor.fetchall()
    print(rs[0])
    #for i in range(1):
        #print(rs[i])
    mycursor.close()
    mydb.close()
    n=input('')
 #*GET ROOM CHARGE**********************************************************   
def roomcharge():
    print("\n\n**WELCOME TO HOTEL ******\n")
    x=(input("Enter your name:"))
    ad=(input("Enter your address:"))
    a=(input("Enter your check in date:"))
    b=(input("Enter your check out date:"))                                                                            
    print("We have the following rooms for you:-")
    print("1.Master Suite---->Rs15000 PN\-")
    print("2.Mini Suite---->Rs10000 PN\-")
    print("3.King---->Rs5000 PN\-")
    print("4.Queen---->Rs4500 PN\-")
    print("5.Quad---->Rs4000 PN\-")
    print("6.Triple---->Rs3000 PN\-")
    print("7.Double---->Rs2500 PN\-")
    print("8.Studio---->Rs1500 PN\-")
    
    x=int(input("Enter Your Choice Please->"))
    b=int(input("Enter you Room no:"))
    n=int(input("Enter the no. of nights you are planning to stay:"))
    if(x==1):
        print("you have opted for Master Suite")
        s=15000*n
    elif(x==2):
        print("you have opted for Mini Suite")
        s=10000*n
    elif(x==3):
        print("you have opted for King")
        s=5000*n
    elif(x==4):
        print("you have opted for Queen")
        s=4500*n
    elif(x==5):
        print("you have opted for Quad")
        s=4000*n
    elif(x==6):
        print("you have opted for Triple")
        s=3000*n
    elif(x==7):
        print("you have opted for Double")
        s=2500*n
    elif(x==8):
        print("you have opted for Studio")
        s=1500*n
    else:
        print("please choose a room")
    print("Your Room charge is:") 
    print(s)
    import  mysql.connector 
    
    mydb=mysql.connector.connect(host ='localhost',user='root',password='1234',db='hotel_management_system')
    mycursor=mydb.cursor()
    mycursor.execute("Update Customers set Total_bill=Total_bill+'%i' where Room_no='%i'"%(s,b))
    mydb.commit()
    mydb.close()
    mycursor.close()
    n=input('')
#-----------------------------------------------------------------------RESTAURANT----------------------------------------------------        
def restaurantbill():
    ts=0
    while(True):
        
         print("RESTAURANT MENU")
         print("1.Water-->Rs20","2.Tea\Coffee-->Rs50","3.Breakfast combo-->Rs250","4.Lunch-->Rs550","Dinner-->Rs1250","6.Exit")
         b=int(input("enter you roomno"))  
         c=int(input("Enter your choice:"))
         d=int(input("Enter the quantity:"))
         s=0
         if (c==1):
             s=20*d
         elif(c==2):
             s=75*d
         elif(c==3):
             s=250*d
         elif(c==4):
             s=550*d
         elif(c==5):
             s=1250*d 
         else:
             print("Exit")
         ts=ts+s
         xyz=input('Do you want to eat more?')
         if(xyz.upper()=='N'):
             break
          
    print('price:',ts)
    import mysql.connector
    
    mydb=mysql.connector.connect(host ='localhost',user='root',password='1234',db='hotel_management_system')
    mycursor=mydb.cursor()
    mycursor.execute("update Customers set Total_bill=Total_bill+'%i' where Room_no='%i'"%(s,b))
    mydb.commit()
    mydb.close()
    mycursor.close()
    n=input('')
#*FITNESS CARE******************************************************
def Fitnesscare():
    import os
    os.system('cls')
    print("1.GYM","2.SPA","3.BAR","4.CASINO","5.SWIMMING POOL","6.Exit")
    b=int(input("enter your roomno"))
    a=int(input("Enter your choice:"))
    if(a==1):
          print("WELCOME TO GYM")
    elif(a==2):
        print("WELCOME TO SPA")
    elif(a==3):
        print("WELCOME TO BAR")
    elif(a==4):
        print("WELCOME TO CASINO")
    elif(a==5):
        print("WELCOME TO SWIMMING POOL")
    else:
       print("Exit")
    n=input('')
def checkout():
    print("THANKS FOR VISITING OUR HOTEL")
    b=int(input("enter your roomno"))
    import  mysql.connector
    mydb=mysql.connector.connect(host ='localhost',user='root',password='1234',db='hotel_management_system')
    mycursor=mydb.cursor()
    mycursor.execute("select Total_bill from Customers where Room_no='%i';"%b)
    r=mycursor.fetchall()
    print("Your Total_bill is:",r[0][0])
    print("Please visit again!!!")
    mycursor.execute("update Customers set Total_bill=0 where Room_no='%i';"%b)
    mydb.commit()
    mydb.close()
    n=input('')
pricebreakup()
Roomno()    
roomcharge()   
restaurantbill() 
Fitnesscare()  
checkout()
