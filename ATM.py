import time
import pickle
from datetime import datetime

def bal_enq():
        time.sleep(1)
        print("your Balance is:",users_data_database[x][1],"PKR")
        print(datetime.now())
        update_database()

def withdraw():
            rs=int(input("Enter the amount you want to withdraw"))
            time.sleep(1)
            if(users_data_database[x][1]>=rs):
                users_data_database[x][1] -=rs
                users_data_database[x][3] +=rs
                print("Amount withdrawn successfully:")
                print(f'''
                        ------------------------------------------
                        RECEIPT
                        ------------------------------------------
                        -NAME : {users_data_database[x][4]}
                        -WITHDRAW AMOUNT : {rs}PKR
                        -DATE and TIME : {datetime.now()}
                        -REMAINING BALANCE: {users_data_database[x][1]}PKR
                        ------------------------------------------
                        ''')
                update_database()
            else:
                print('''
                        -------------------
                             WARNING!!!
                        INSUFFICIENT BALANCE
                        -------------------
                        ''')

def deposit():
    rs=int(input("Enter the amount you want to deposit"))
    users_data_database[x][1] +=rs
    users_data_database[x][2] +=rs
    print("Amount deposit successfully:")
    print(f'''
          --------------------------------------------
          RECEIPT
          --------------------------------------------
          -NAME : {users_data_database[x][4]}
          -DEPOSIT AMOUNT : {rs}PKR
          -DATE and TIME : {datetime.now()}
          -NEW BALANCE: {users_data_database[x][1]}PKR
          --------------------------------------------
          ''')
    update_database()

def history():
    print("your credit amount is=",users_data_database[x][2],"PKR")
    print("your debit amount is=",users_data_database[x][3],"PKR")

def update_database():
    database = open("data.pkl", "wb")
    pickle.dump(users_data_database, database)
    database.close()

def sign_up():
    for z in range(2):
            number = str(input("Enter the account number:\n"))
            if number not in users_data_database.keys():
                    n=len(number)
                    if(n==9):
                            name = input("Enter the Name of Customer:\n")
                            pin = str(input("Enter the Account PIN\n"))
                            m=len(pin)
                            if(m==4):
                                    new_user_data = [pin, 0, 0, 0, name]
                                    users_data_database[number] = new_user_data
                                    update_database()
                                    print('Congartulations"\nNew User Account created Successfully!\n')
                            else:
                                print("pin should be foure digit")
                            
                    else:
                        print("account number should be nine digit")
            else:
                print("The account number already exist\n Please try with new account number")
                exit()
    

# users_data_database={
#     "123456789":[1234 , 0 , 0, 0 ,"KASHIF"],
#     "987654321":[1235 , 5000 , 2500 , 3000 ,"talal"],
#     "123789456":[1248 , 5000 , 2000 , 5000 ,"basit"],
# }

# ************ To load the data from database ************

a_file = open("data.pkl", "rb")

users_data_database = pickle.load(a_file)

print(users_data_database)


print("**********************")
print("Welcome to ATM")
print("**********************")

value = input("Select the Option: \n1- Login\n2- Sign Up\n>>>>>")
value = int(value)
if value == 1:
    pass
elif value == 2:
    sign_up()
    exit()
else:
    exit()

for I in range(3):
        x=input("Enter the account number\n")
        if x in users_data_database.keys():
            for J in range(3):
                    pin=input("Enter your pin:")
                    if pin== users_data_database[x][0]:
                        # time.sleep(2)
                        while True:
                            print("**********************")
                            print()
                            print("1-Balance Inquiry")
                            print("2-Cash withdraw")
                            print("3-Deposit money")
                            print("4-transcation history")
                            print("5-Exit")
                            print()
                            print("**********************")
                            ch=int(input("Enter your choice :"))
                            if(ch==1):
                                k=bal_enq() 
                            elif(ch==2):
                                k=withdraw()
                            elif(ch==3):
                                k=deposit() 
                            elif(ch==4):
                                k=history()
                            elif(ch==5):
                                print('''
                                      ------------------------------- 
                                                 THANK YOU
                                      FOR CHOOSING OUR BANKING SYSTEM
                                      -------------------------------
                                      ''')
                                exit()
                            else:
                                print("Enter valid option")
                    else:
                        print('''
                                -------------
                                  WARNING!!!
                                 INVALID PIN
                                -------------
                                ''')
        else:
            print('''
                   ----------------
                      WARNING!!!
                   INVALID ACCOUNT
                   ----------------
                   ''')

