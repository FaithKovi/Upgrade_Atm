import datetime
import random

database = {'1597059360': ('Faith', 'Kovi', 'faithk@gmail.com', 2345), '1592159160': ('Emma', 'Wach', 'emmaw@gmail.com', 2712), '1597059360': ('Gigi', 'Ken', 'gigik@gmail.com', 4213) }

current_balance = 50000


def withdrawal_operation():
    global current_balance
    withdraw = int(input("How much would you like to withdraw? \n"))
    if (withdraw > (current_balance - 1)):
        print("You have insufficient funds")
    elif (withdraw <= (current_balance - 1)):
        current_balance -= withdraw
        print("Your new balance: %d "%current_balance)
        print("Take your cash")
    else:
        print("Error processing request")
        withdrawal_operation()
        

def deposit_operation():
    global current_balance
    deposit = int(input("How much would you like to deposit? \n"))
    current_balance += deposit
    print("Your current balance : %d "%current_balance)


def complaint_operation():
    complaint = input("What issue would you like to report? \n")
    print("Thank you for contacting us")


def bank_operation(user_details):
    print("Welcome %s %s " % ( user_details[0], user_details[1] ) )
    selected_option = int(input("What operation do you want to perform: \n 1. Withdraw \n 2. Deposit \n 3. Complaint \n 4. Logout \n"))
    if (selected_option == 1):
        withdrawal_operation()
    elif (selected_option == 2):
        deposit_operation()
    elif (selected_option == 3):
        complaint_operation()
    elif (selected_option == 4):
        next_transaction = int(input("Do you want to perform another transaction? \n 1. Yes \n 2. No"))
        if next_transaction == 1:
            login()
        elif next_transaction == 2:
            print("Thank you for banking with us!!!")
        else:
            print("Input a valid option")
    else:
        print("Invalid option selected")
        bank_operation(user_details)


def login():
    print("***** LOGIN *****")
        
    account_number_from_user = int(input("What is your account number? \n"))
    password = int(input("What is your 4 digits password? \n"))

    for account_number, user_details in database.items():
        if (account_number == account_number_from_user):
            if (user_details[3] == password):
                bank_operation(user_details)
            else:
                print("Invalid account number or password!")
                login()
        


def generate_accountNumber():
    return random.randrange(1111111111,9999999999)


def register():
    print( "* REGISTER *" )
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = int(input("Create a 4 digit pin for yourself \n"))

    account_number = generate_accountNumber()
    user_details = (first_name, last_name, email, password) 
    database[account_number] = user_details
    print("Your Account has been created")
    print(" * * ** *")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" ***** ***** ****")

    login()


def init():
    print("Welcome to bank PY")
    now = datetime.datetime.now()
    print("Current date and time is:")
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    
    have_account = int(input("Do you have an account with us: \n 1. (Yes) \n 2. (No) \n"))

    if (have_account == 1):
        login()
    elif(have_account == 2): 
        register()
    else:
        print("You have selected an invalid option")
        init()


###MAIN BANKING SYSTEM ###
init()