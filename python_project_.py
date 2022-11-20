import time
print("please inseart your card")
#for card processing
time.sleep(2)
password=7488
#taking atm pin from user
pin=int(input("Enter your atm pin:    "))

#user account balance
balance=10000

#checking pin is valid or not
if pin==password:
    #loop will run user get free
    while True:
        #showing info of user
        print("""
        1-balance
        2-withdraw cash
        3-deposit cash
        4-exit
        
        """)
        try:
            #taking an option from user
            option=int(input("please entern your choice: "))
        except:
            print("please enter valid option")
         #for option 1
        if option==1:
            print(f"your current balance is{balance}")
        if option==2:
            withdraw_amount=int(input("please enter withdraw_amount: "))
            if balance>withdraw_amount:
                balance=balance-withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"your updated balance is{balance}")
            else:
                print("please enter valid amount")
        if option==3:
            deposit_amount=int(input("please enter deposit_amount: "))
            balance=balance+deposit_amount
            print(f"{deposit_amount}is credited to yuor account")
            print(f"your updated balance is{balance}")
        if option==4:
            break
        if balance<=1000:
            print("Low balance")
else:
    print("wrong pin please try again")