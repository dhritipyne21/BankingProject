import random
import datetime
import cx_Oracle
con = cx_Oracle.connect('system/qwerty97@127.0.0.1/XE')
print(con.version)
cur = con.cursor()

flag=0
no=random.randint(10000,90000)
ac=[]
accno="BANK"+str(no)
cust="CUST"+str(no)

while True:
    print("Main Menu")
    print("1. Sign Up (New Customer)")
    print("2. Sign In (Existing Customer)")
    print("3. Admin SignIn")
    print("4. Quit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        fname=input("Enter first name: ")
        lname=input("Enter last name: ")
        address=input("Enter address:")
        dob=input("Enter D.O.B : D-M-Y")
       #try:
        #    datetime.datetime.strptime(dob, '%d-%m-%Y')
        #except ValueError:
         #   raise ValueError("Incorrect data format, should be YYYY-MM-DD")'''
        cno=int(input("Enter contact no. :"))
        email=input("Enter email : ")
        cid="CUST"+str(no)
        accno="BANK"+str(no)
        act=input("Enter account type\n1.1:Current\n1.2:Savings\n\nEnter your choice: ")
        if act=='1.1':
            at='Current'
            b=int(input("Make a deposit:"))
            if b<5000:
                print("Minimum deposit is 5000")
                b=int(input("Make a deposit:"))
        elif act=='1.2':
            at='Savings'
            b=int(input("Make a deposit:"))
        else:
            print("Invalid option.")
            break
        print("Your customer_id :  ",cid)
        print("Your account_number :  ",accno)
        password=input("Set your password (min 8 alpha-numeric characters):")
        while(len(password)<8 or password.isalnum()==False):
            password=input("Set your password (min 8 alpha-numeric characters):")
        qs='''insert into customer(Customer_ID,Account_Number,Account_Type,Password,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID,Balance,Status) values (:Customer_ID,:Account_Number,:Account_Type,:Password,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID,:Balance,0)'''       
        cur.execute(qs,Customer_ID=cid,Account_Number=accno,Account_Type=at,Password=password,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email,Balance=b)
        con.commit()
        print("Account successfullly created")
        
    if ch == 2:
        ll=0
        cid=input("Enter Customer id :")
        qs='''select status from customer where Customer_ID=:Customer_ID'''
        cur.execute(qs,Customer_ID=cid)
        for result in cur:
           ll=result[0]
        if(ll==1):
            print("Sorry your account is locked")
            break
        else:
            password = input("enter your password : ")
        
            count=0
            while(count<3):
                #if password matches
                qs='''select Password from customer where Customer_ID= :Customer_ID'''
                cur.execute(qs,Customer_ID=cid)
                con.commit()
                for result in cur:
                    p= result[0]
                if(password==p): 
                #if(password == 'abcd'): #just a test password
                    print ("Successfull Login ")
                    l=[]
                    qs='''select Account_Number from customer where Customer_ID=:Customer_ID'''
                    cur.execute(qs,Customer_ID=cid)
                    for result in cur:
                        l.append(result[0])
                    while True:
                        print ("Menu : ")
                        print("2.1 Address change")
                        print("2.2 Open account")
                        print("2.3 Deposit Money")
                        print("2.4 Withdraw Money")
                        print("2.5 Transfer Money")
                        print("2.6 Print Receipt")
                        print("2.7 Account Closure")
                        print("2.8 Avail Loan")
                        print("2.9 Customer logout")
                        print("2.10 Back")
                        ch2 = input("Enter Choice ")
                        if(ch2 == "2.1"):
                            address=input("Enter Address:")
                            qs='''update customer set Address= : Address  where Customer_ID= :Customer_ID'''
                            cur.execute(qs,Address=address,Customer_ID=cid)
                            con.commit()
                            print("Address changed successfully!!")
                            #sql query to change address
                            break
                        elif(ch2 == "2.2"):
                            print("Open new account ")
                            qs='''select customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID from customer where Customer_ID= :Customer_ID'''
                            cur.execute(qs,Customer_ID=cid)
                            for result in cur:
                                fname=result[0]
                                lname=result[1]
                                dob=result[2]
                                address=result[3]
                                cno=result[4]
                                email=result[5]
                            con.commit()
                            print("2.2.1 Open CA")
                            print("2.2.2 Open SA")
                            print("2.2.3 Open FD")
                            ch21 = input("enter choice")
                            if(ch21 == "2.2.1"):
                                print("CA ACCOUNT")
                                accno="BANK"+str(no)
                                print("Your account_number :  ",accno)
                                #SQL query to insert
                                at='Current'
                                accno="BANK"+str(no)
                                b=int(input("Make a deposit:"))
                                if b<5000:
                                    print("Minimum deposit is 5000")
                                    b=int(input("Make a deposit:"))
                                qs='''insert into customer(Customer_ID,Account_Type,Account_Number,Password,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID,Balance,Status) values (:Customer_ID,:Account_Type,:Account_Number,:Password,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID,:Balance,0)'''       
                                cur.execute(qs,Customer_ID=cid,Account_Type=at,Account_Number=accno,Password=password,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email,Balance=b)
                                con.commit()        
                             
                                break
                            elif(ch21 == "2.2.2"):
                                print("SA ACCOUNT")
                                accno="BANK"+str(no)
                                print("Your account_number :  ",accno)
                                #sql query to insert
                                at='Savings'
                                accno="BANK"+str(no)
                                b=int(input("Make a deposit:"))
                                qs='''insert into customer(Customer_ID,Account_Type,Account_Number,Password,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID,Balance,Status) values (:Customer_ID,:Account_Type,:Account_Number,:Password,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID,:Balance,0)'''       
                                cur.execute(qs,Customer_ID=cid,Account_Type=at,Account_Number=accno,Password=password,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email,Balance=b)
                                con.commit() 
                             
                                break
                            elif(ch21 == "2.2.3"):
                                print("FD account")
                                #sql query to insert
                                at='Fixed'
                                amount=int(input("Enter amount to be deposited"))
                                term=int(input("enter Number of months"))
                                if(amount<0 or term<12 or (amount%1000)!=0):
                                    print("invalid amount/term")
                                    print("enter amount as multiple of 1000 and term>12")
                                    amount=int(input("Enter amount to be deposited"))
                                    term=int(input("enter Number of months"))
                                print("Amount fixed")
                                accno="BANK"+str(no)
                                print("Your account_number :  ",accno)
                                qs='''insert into customer(Customer_ID,Account_Type,Account_Number,Password,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID,Balance,Status) values (:Customer_ID,:Account_Type,:Account_Number,:Password,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID,0,0)'''       
                                cur.execute(qs,Customer_ID=cid,Account_Type=at,Account_Number=accno,Password=password,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email)
                                con.commit() 
                             
                                qs='''insert into fixed (Customer_ID,Account_Number,Amount,Terms) values (:Customer_ID,:Account_Number,:Amount,:Terms)'''
                                cur.execute(qs,Customer_ID=cid,Account_Number=accno,Amount=amount,Terms=term)
                                con.commit()
                             #sql query to show all FD by that customer
                                break
                            else:
                                print("wrong choice")
                                break
                         
                        elif(ch2 == "2.3"):
                            au=0
                            amt=0
                            a=0
                            ano=input("enter account number to be deposited to")
                            if(ano in l):
                                 amt=int(input("enter amount to be deposited"))
                                 #a=#fetch current balance from database
                                 if(amt<0):
                                     print("amount cannot be negative")
                                     amt=int(input("enter amount to be deposited"))
                                 qs='''select Balance from customer where Customer_ID=:Customer_ID and Account_Number=:Account_Number'''
                                 cur.execute(qs,Account_Number=ano,Customer_ID=cid)
                                 for result in cur:
                                     a=result[0]
                                 au=a+amt
                                 qs='''insert into statement(customer_id,Account_Number,Updation_date_time,debit,credit,previous_balance,updated_balance) values(:customer_id,:Account_number,to_date(sysdate,'dd/mm/yyyy'),:debit,0,:previous_balance,:updated_balance)'''
                                 cur.execute(qs,customer_id=cid,Account_number=ano,debit=amt,previous_balance=a,updated_balance=au)
                                 con.commit()
                                 qs='''update customer set Balance= :Balance where Customer_ID= :Customer_ID and Account_number= :Account_number'''
                                 cur.execute(qs,balance=au,Customer_ID=cid,Account_number=ano)
                                 con.commit()
                                 print("Amount Deposit done")
                                 
                        #update database
                        #query to print amount
                        elif(ch2 == "2.4"):
                             #sql query to withdraw money
                             print("Withdraw")
                             ano=input("Enter account number:")
                             w=int(input("enter amount to withdraw"))
                             wa=0
                             qs='''select Account_Type from customer where Account_Number=:Account_Number and  Customer_ID= : Customer_ID'''
                             cur.execute(qs,Account_Number=ano, Customer_ID=cid)
                             for result in cur:
                                 at=result[0]
                             #a=#fetch current balance from database
                             qs='''select balance from customer where Customer_ID=:Customer_ID and Account_Number= :Account_Number'''
                             cur.execute(qs,Account_Number=ano, Customer_ID=cid)
                             for result in cur:
                                 a=result[0]
                             b=a-w
                             if (at=='Current'):
                                 if(w<0):
                                     print("invalid amount")
                                 elif b<5000:
                                     print("Insufficient balance")
                                 else:
                                     wa=w
                                 
                             elif at=='Savings':
                                 if (w>a):
                                     print("Insufficient balance")
                                 elif(w<0):
                                     print("invalid amount")
                                 else:
                                     wa=w
                             else:
                                 print("Invalid account number!")
                             qs='''insert into statement(customer_id,Account_Number,Updation_date_time,debit,credit,previous_balance,updated_balance) values(:customer_id,:Account_number,to_date(sysdate,'dd/mm/yyyy'),0,:credit,:previous_balance,:updated_balance)'''
                             cur.execute(qs,customer_id=cid,Account_number=ano,credit=w,previous_balance=a,updated_balance=b)
                             con.commit()
                             qs='''update customer set balance= :balance where Customer_ID= :Customer_ID and Account_number= :Account_number'''
                             cur.execute(qs,balance=b,Customer_ID=cid,Account_number=ano)
                             con.commit()
                             print("Withdraw complete")
                             
                             #update database with amount
                             #sql query to print amount
                             break
                        elif(ch2 == "2.5"):
                             #sql query to transfer monneygo
                             print("transfer")
                             from_cid=input("Enter the customer id from which money is to be transferred: ")
                             from_ano=input("Enter account number: ")
                             to_cid=input("Enter the customer id to which money is to be transferred: ")
                             to_ano=input("Enter account number: ")
                             #amount=int(input("enter the amount to be transferred"))
                             if(from_cid==cid and from_ano in l):
                                 tb=0
                                 fb=0
                                 sum=int(input("Enter sum: "))
                                 qs='''select updated_balance from statement where Customer_ID= :Customer_ID and Account_Number= :Account_Number'''
                                 cur.execute(qs,Customer_ID=to_cid,Account_Number=to_ano)
                                 con.commit()
                                 for result in cur:
                                     tb=result[0]
                                 t=tb+sum
                                 qs='''select updated_balance from statement where Customer_ID= :Customer_ID and Account_Number= :Account_Number'''
                                 cur.execute(qs,Customer_ID=from_cid,Account_Number=from_ano)
                                 con.commit()
                                 for result in cur:
                                     fb=result[0]
                                 if(fb<sum):
                                     print("Insufficient balance.")
                                     break
                                 f=fb-sum
                                 qs='''insert into statement(customer_id,Account_Number,Updation_date_time,Credit,previous_balance,updated_balance) values(:customer_id,:Account_number,to_date(sysdate,'dd/mm/yyyy'),:Credit,:previous_balance,:updated_balance)'''
                                 cur.execute(qs,customer_id=to_cid,Account_number=to_ano,Credit=sum,previous_balance=tb,updated_balance=t)
                                 con.commit()
                                 qs='''update customer set balance= :balance where Customer_ID= :Customer_ID and Account_number= :Account_number'''
                                 cur.execute(qs,balance=t,Customer_ID=to_cid,Account_number=to_ano)
                                 con.commit()
                                 print("Transferred to: ",to_cid)
                                
                                 qs='''insert into statement(customer_id,Account_Number,Debit,Updation_date_time,previous_balance,updated_balance) values(:customer_id,:Account_number,:Debit,to_date(sysdate,'dd/mm/yyyy'),:previous_balance,:updated_balance)'''
                                 cur.execute(qs,customer_id=from_cid,Account_number=from_ano,Debit=sum,previous_balance=fb,updated_balance=f)
                                 con.commit()
                                 qs='''update customer set balance= :balance where Customer_ID= :Customer_ID and Account_number= :Account_number'''
                                 cur.execute(qs,balance=f,Customer_ID=from_cid,Account_number=from_ano)
                                 con.commit()
                                 print("Transfer done")
                                 
                                
                             else:
                                 print("Invalid customer id.")
                             break
                         #c=#account of user logged in
                         #if(af!=c):
                         #   print("invalid transaction")
                         #print updated value of both account
                         #update accounts
                    
                        elif(ch2 == "2.6"):
                            acc=input("Account Number: ")
                            date1=input("enter date from (D-M-Y):")
                    
                             
                            date2=input("enter date to (D-M-Y):")
                            flag=0
                             
                             
                            if(date2>date1):
                                qs='''select * from statement where Customer_ID=:Customer_ID and Account_Number= :Account_Number and updation_date_time between to_date(:l1,'dd-mm-yyyy') and to_date(:l2,'dd-mm-yyyy')'''
                                cur.execute(qs,Customer_ID=cid,Account_Number=acc,l1=date1, l2=date2)
                                for result in cur:
                                    print("Customer ID: ",result[0])
                                    print("Account_Number:",result[1])
                                    print("Updated on: ",result[2])
                                    print("Credit ",result[3])
                                    print("Debit ",result[4])
                                    print("Previous Balance ",result[5])
                                    print("Updated Balance ",result[6])
                                    flag=1
                                if flag==1:
                                    print("receipt printed")
                                else:
                                    print("invalid account")
                            break
                        elif(ch2 == "2.7"):
                             #sql query to close the account
                             print("account close")
                             ano=input("Enter account no:")
                             qs='''select * from customer where Customer_ID= :Customer_ID and Account_Number= :Account_Number'''
                             cur.execute(Customer_ID=cid,Account_Number=ano)
                             con.commit()
                             for result in cur:
                                 c_id=result[0]
                                 pwd=result[1]
                                 at=result[2]
                                 an=result[3]
                                 fname=result[4]
                                 lname=result[5]
                                 dob=result[6]
                                 address=result[7]
                                 cno=result[8]
                                 email=result[9]
                                 #sql query to close the account
                             qs='''insert into closedaccount(Customer_ID,Password,Account_Type,Account_Number,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID,closing_date_time) values (:Customer_ID,:Password,:Account_Type,:Account_Number,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID,to_date(sysdate,'dd/mm/yyyy hh24:mi:ss'))'''       
                             cur.execute(qs,Customer_ID=c_id,Password=pwd,Account_Type=at,Account_Number=an,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email)
                             con.commit()
                             qs='''delete from customer where Customer_ID=:Customer_ID and Account_Number=:Account_Number '''       
                             cur.execute(qs,Customer_ID=c_id,Account_Number=ano)
                             con.commit()
                             break
                        elif(ch2 == "2.8"):
                            b=0
                            acc=input("Enter account number:")
                            amount=int(input("enter the loan amount"))
                            term=int(input("enter the avail term"))
                            if(amount<0 or (amount%1000)!=0 or term<0):
                                print("amount or term must not be negative and should be a multiple of 1000")
                                amount=int(input("enter the loan amount"))
                                term=int(input("enter the avail term"))
                                acc=input("Enter your savings account number: ")
                            qs='''select Balance,Account_Type from customer where Customer_ID= :Customer_ID and Account_Number=:Account_Number '''
                            cur.execute(qs,Customer_ID=cid,Account_Number=acc)
                            for result in cur:
                                if result[1]=='Savings':
                                    b=result[0]
                                else:
                                    print("Invalid account.")
                                    break
                        #balance=sql query to fetch balance from savings account
                            if(amount<=2*b):
                                qs='''select customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID from customer where Customer_ID= :Customer_ID'''
                                cur.execute(qs,Customer_ID=cid)
                                for result in cur:
                                    fname=result[0]
                                    lname=result[1]
                                    dob=result[2]
                                    address=result[3]
                                    cno=result[4]
                                    email=result[5]
                                #sql query to update the loan table
                                at='Loan'
                                accno="BANK"+str(no)
                                qs='''insert into customer(Customer_ID,Account_Type,Account_Number,Password,customer_fame,customer_lame,Date_of_Birth,Address,Contact,Email_ID) values (:Customer_ID,:Account_Type,:Account_Number,:Password,:customer_fame,:customer_lame,:Date_of_Birth,:Address,:Contact,:Email_ID)'''       
                                cur.execute(qs,Customer_ID=cid,Account_Type=at,Account_Number=accno,Password=password,customer_fame=fname,customer_lame=lname,Date_of_Birth=dob,Address=address,Contact=cno,Email_ID=email)
                                con.commit() 
                             
                                qs='''insert into loan (Customer_ID,Account_Number,Amount,Terms) values (:Customer_ID,:Account_Number,:Amount,:Terms)'''
                                cur.execute(qs,Customer_ID=cid,Account_Number=accno,Amount=amount,Terms=term)
                                con.commit()
                                print("Loan granted")
                            else:
                                print("You cannot avail this loan")
                            break
                        elif(ch2 == "2.9"):
                            print("Logout Successfully")
                            break
                        elif(ch2 == "2.10"):
                            break
                        else:
                            print("Invalid option")
                            break
                    flag=1
                    break
                else:
                    count=count+1
                    print("try again")
                    password = input("enter your password : ")
        if(count==3):
            qs='''update customer set status=1 where Customer_ID=:Customer_ID '''
            cur.execute(qs,Customer_ID=cid)
            con.commit()
        #    account='locked'#update  locked account table as 1
        #'''if(flag==1):
         #   break'''


    if(ch==3):
        aid = input("Enter admin id : ")
        password = input("enter password ; ")
        qs='''select password from admin where id=:id'''
        cur.execute(qs,id=aid)
        for result in  cur:
            if result[0]==password:
                print("Logged in successfully!")
            else:
                print("Incorrect Password")
                break
        fd=[]
        qs='''select Customer_ID from fixed '''
        cur.execute(qs)
        for result in cur:
            fd.append(result[0])
        loan=[]
        qs='''select Customer_ID from loan '''
        cur.execute(qs)
        for result in cur:
            loan.append(result[0])
                
        print("Menu : ")
        print("3.1 Closed Accout History")
        print("3.2 FD report of a customer")
        print("3.3 FD report of a customer vis a vis another customer")
        print("3.4 FD report w.r.t a particular account")
        print("3.5 Loan report o a customer")
        print("3.6 Loan report o a customer vis a vis another customer")
        print("3.7 Load report w.r.t a particular amount")
        print("3.8 Load-FD report of customers")
        print("3.9 Report of customers who are yet to avail a loan")
        print("3.10 Report of customers who are yet to open an FD account")
        print("3.11 Report of customers who neither have a loan nor a FD account in bank")
        print("3.12 Admin logout ")
        ch3 = input("Enter choice")
        if(ch3 == "3.1"):
            #sql query to print closed account
            cid=input("Enter ")
            qs='''select * from closedaccount '''
            cur.execute(qs)
            for result in cur:
                print("Customer id: ",result[0])
                print("Password",result[1])
                print("Account type: ",result[2])
                print("Account number",result[3])
                print("First name",result[4])
                print("Last name",result[5])
                print("D.O.B :",result[6])
                print("Address: ",result[7])
                print("Contact no: ",result[8])
                print("Email: ",result[9])
                print("Closed on: ",result[10])
            print("closed account")
        elif(ch3 == "3.2"):
            #sql query to print FD report of a customer"
            cid=input("enter customer id:")
            if cid in fd:
                qs='''Select * from fixed where Customer_ID=:Customer_ID '''
                cur.execute(qs,Customer_ID=cid)
                con.commit()
                for result in cur:
                    print(result)
        elif(ch3 == "3.3"):
            # sql query to find FD report of a customer vis a vis another customer
            print("FD report")
            cid=input("enter customer id:")
            amt=0
            if cid in fd:
                qs='''Select Amount from fixed where Customer_ID=:Customer_ID '''
                cur.execute(qs,Customer_ID=cid)
                con.commit()
                for result in cur:
                    amt=result[0]
                qs='''Select * from fixed where Amount>= :Amount '''
                cur.execute(qs,Amount=amt)
                con.commit()
                for result in cur:
                    print(result)
            
        elif(ch3 == "3.4"):
            amt = ("enter amount:")
            if(amt<0 or (amt%1000)!=0):
                print("invalid amount")
                amt = int(input("enter amount:"))
                qs='''Select * from fixed where Amount>= :Amount '''
                cur.execute(qs,Amount=amt)
                con.commit()
                for result in cur:
                    print(result)
            #sql query to print FD report w.r.t a particular account
            print("done")
        elif(ch3 == "3.5"):
            #sql query to find  Loan report o a customer
            cid=input("enter customer id:")
            amt=0
            if cid in loan:
                qs='''Select * from loan where Customer_ID=:Customer_ID '''
                cur.execute(qs,Customer_ID=cid)
                con.commit()
                for result in cur:
                    print(result)
        elif(ch3 == "3.6"):
            cid=input("enter customer id:")
            amt=0
            if cid in loan:
                qs='''Select Amount from loan where Customer_ID=:Customer_ID '''
                cur.execute(qs,Customer_ID=cid)
                con.commit()
                for result in cur:
                    amt=result[0]
                qs='''Select * from loan where Amount>= :Amount '''
                cur.execute(qs,Amount=amt)
                con.commit()
                for result in cur:
                    print(result)
            #sql query to find if the customer has a loan
            #sql query to display all customers who have a loan greater than the amount of the customer
        elif(ch3 == "3.7"):
            print("respect a particular amount")
            amt = ("enter amount:")
            if(amt<0 or (amt%1000)!=0):
                print("invalid amount")
                amt = int(input("enter amount:"))
                qs='''Select * from fixed where Amount>= :Amount '''
                cur.execute(qs,Amount=amt)
                con.commit()
                for result in cur:
                    print(result)
            #display all customers having load amount>amount
        elif(ch3 == "3.8"):
            print("Loan-FD report")
            #sql query to find Loan-FD report of customers
            qs='''select Customer_ID from from loan,fixed where loan.Customer_ID==fixed.Customer_ID, loan.sum(Amount)>fixed.sum(Amount) group by Customer_ID '''
            cur.execute(qs,Amount=amt)
            con.commit()
            for result in cur:
                print(result[0])
        elif(ch3 == "3.9"):
            print("yet to avail a loan")
            qs='''select Customer_ID from from customer where Customer_ID not in (select  Customer_ID from loan)'''
            cur.execute(qs)
            con.commit()
            for result in cur:
                print(result)
            #sql query to find Report of customers who are yet to avail a loan
        elif(ch3 =="3.10"):
            print("yet to avail FD-account")
            qs='''select Customer_ID from from customer where Customer_ID not in (select  Customer_ID from fixed)'''
            cur.execute(qs)
            con.commit()
            for result in cur:
                print(result)
            #sql query to find Report of customers who are yet open an FD account
        elif(ch3 == "3.11"):
            print("neither loan nor FD account")
            qs='''select Customer_ID from from customer where Customer_ID not in (select  Customer_ID from loan) and Customer_ID not in (select  Customer_ID from fixed)'''
            cur.execute(qs)
            con.commit()
            for result in cur:
                print(result)
            #sql query to find Report of customers who neither have a loan nor a FD account in bank
            
        elif(ch3 == "3.12"):
            print("Admin successfully logged out")
        else:
            print("invalid input")

                         
    elif(ch==4):
        break              


con.commit()
cur.close()
con.close()
        
            
        
                     
                    
        

            
            
