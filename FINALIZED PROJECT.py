bike={}
customer =[]
sale = []
record=0
def add_bike():
    global record # can be used anywhere
    while True:# unless it is true it will run
        n=input("Bike Owner Name  ") # Enter owner name for bike
        cc=(eval(input("Engine Power in CC   ")))  # Enter cc name for bike
        ch=int(input("Enter the Chassis Number of Bike  "))#Enter engine power for bike
        mo=eval(input("Bike Model   "))#Enter model for bike
        bike[n]=[cc,ch,mo] # assigning values to the bike
        record = 1# if record is 1 it execute to next line which is com
        com = input('Do you want to add more records(yes or no)   ') # asks user if he wants to more records  
        if com == 'yes':# it will run if yes is typed
            continue # it will move it back to the loop
        else:# otherwise this satement execute 
            break
def view_bike(): # creating a user defined function for viewing records
    global record # can be used anywhere
    if record>0 :  # it runs if record is greater than 0
        print('  View Records  ') # heading ( just for output to look nice)
        print("Owner Name \t Engine Power \t\t Chassis Number.\t\t Bike Model ") # showing output in tabular form
        for i in bike.keys():  # showing results in sequence
            mylist=bike[i] # storing bike first index record in mylist 
            print(i, '\t\t', mylist[0], '\t\t\t', mylist[1],'\t\t\t\t', mylist[2]) # display the record (id, name, number, adress)accord to their corresponding index values
    else: # runs if the previous statement dont satisfies
        print('No Bike record exist') # tell the user that there is no record avaiable to view
def edit_bike(): # creating a user defined function for editing records
    global record # can be used anywhere
    if record>0 : # it runs if record is greater than 0
        x=input("enter owner name you want to edit record of  ") # enter owner name you want to edit
        if x in bike.keys(): # it runs if x in bikes dictionary
            cc=(eval(input("Engine Power in CC  "))) # Enter engine power of bike
            ch=int(input("Enter the Chassis Number of Bike  ")) # Enter chassis no of bike
            mo=eval(input("Bike Model  ")) # Enter model of bike
            bike[x]=[cc,ch,mo] # adding edited records in dictionary
        else: # runs if the previous statement dont satisfies
            print("no record found") # tell the user that no record is found for your typed name
    else: # runs if the previous statement dont satisfies
        print("enter record first") # tell the user that he has to enter record first
def search_bike(): # creating a user defined function for searching records
    global record # can be used anywhere
    if record>0:  # it runs if record is greater than 0
        y=input("enter owner name you want to search record of  ") # enter the owner name of bike you want to search
        if y in bike.keys(): # if y in bikes named dictionary then it will run
            lst=bike[y] 
            print("Owner Name \t Engine Power \t\t Chassis Number.\t Bike Model ") # printing in tabular form
            print(y,"\t\t",lst[0],"\t\t\t",lst[1],"\t\t\t",lst[2]) # printing in sequence
        else: # if previous condition dont runs
            print("no such bike owner found ") # if owner is not found
    else: #if previous condition dont runs
        print("please enter record first") # tell the user that he has to enter record first
def delete_bike(): # creating a user defined function for deleting records
    global record # can be used anywhere
    if record>0:  # it runs if record is greater than 0
        y=input("enter owner name you want to delete record of  ") # enter the owner name of bike you want to delete
        if y in bike.keys(): # if y in bikes named dictionary then it will run
            del bike[y] # delete bikes y whole list
        else: # if previous condition dont runs
            print("no such bike owner found") # if written owner is not present
    else:  # if previous condition dont runs
        print("please enter record first") # tell the user that he has to enter record first


def bike_menu():  # menu function definition
    while True: # if condition satisfies then following runs
        print("""Press 1 to Add bike
Press 2 to View bike
Press 3 to Edit bike
Press 4 to Search bike
Press 5 to Delete bike
Press 6 for the main menu""") # display the functions user can perform
        ask = eval(input('Enter Corresponding Number to Perform Desired Task: ')) # ask user what function he wants to perform
        if ask == 1:  # if user types 1
            print('Add bike') # tell the user that he is going to add Customers
            add_bike() # calls the add function
             # exits the program
        elif ask == 2: # if user types 2
            print('View bike') # tell the user that he is going to view customers
            view_bike()
        elif ask == 3: # if user types 3
            print('Edit bike') # tell the user that he is going to use edit function
            edit_bike() # calls the edit function
        elif ask == 4: # if user types 4
            print('Search for bike') # tell the user that he is going to use search function
            search_bike() # calls the search function
        elif ask == 5: # if user types 5
            print('Delete bike') # tell the user that he is going to use delete function
            delete_bike() # calls the delete function
        elif ask == 6: # it is executed when user type 6
            menu()
        else: # if user types something that was not expected
            print('Please enter a valid number') # tell the user that he has to enter valid number
            bike_menu()  # call the menu() function again to display the menu for user
        
#print('BIKE RECORD  ^_^ ') #display the heading



def add_customer():
    while True:
        customer.append(input('Customer Name: '))
        customer.append(input('Customer Id: '))
        customer.append(input('Customer No: '))
        customer.append(input('Customer City: '))
        confirm=input('Do you want to enter data yes or no: ')
        if confirm =='yes':
            add_customer()
        else:
            customer_menu()

def view_customer():
    if customer:
        print('Viewing Record')
        print("Customer_Name\t\t\tCustomer_ID\t\t\tCustomer_Address\t\t\tCustomer_City")
        for i in range(0,len(customer),4):
            print(customer[i], '\t\t\t', customer[i + 1], '\t\t\t', customer[i + 2], '\t\t\t\t', customer[i + 3])
        customer_menu()
    else:
        print("No Customer Record Exist. ADD FIRST!")
        customer_menu()
        
def edit_customer(): # defining edit function
    if customer: # if there is record then edit it else just dont do it cuz there is no record to be edited
        found = False # intializing a variable to keep a track if the item user wants to edit is found or not
        q = input('Enter Customer Name ')  # search the item if it exists
        for i in range(0, len(customer), 4):  # loop through those index values that have Sales Id in the Customer List
            if q == customer[i]:
                found = True # change found to be True,i.e , searched sales id is found
                value = i # keep the track of index so to be used in editing that specific record value
                break  # if found then break out of loop , as there is unique Sales id for every Customer
        if found:
            print('Your Searched Customer Found!')
            editno1 = input('Enter New CustomerID ')  # ask the user what value he wants to replace with
            customer[i + 1] = editno1  # replace the phone number with new value entered by user         
            editno2 = input('Enter New Phone number of Customer ')  # ask the user what value he wants to replace with
            customer[i + 2] = editno2  # replace the phone number with new value entered by user                    editno3 = input('Enter city of Customer ')  # ask the user what value he wants to replace with
            editno3 = input('Enter New City_Customer ')
            customer[i + 3] = editno3  # replace the phone number with new value entered by user
            print('Customer Id: ', q, ' has been edited to ' + editno1)
            print('Customer Address: ', q, ' has been edited to ' + editno2)
            print('City is ', q, ' has been edited to ' + editno3)
            customer_menu()  # go to main menu after edting has been done by calling menu() function
        else:
            print('Searched Customer not found') # tell the user that searched id that user wants to edit hasn't been found 
            customer_menu() # call the menu function to return back to main menu() again
    else:
        print('No Customer Record is there to edit.ADD FIRST')  # display that there is no record to be edited
def search_customer(): # defining search function
    if customer:
        found = False  # intializing a variable to keep a track if the searched item is found or not
        search = input('Enter Sales ID you want to search for ')  # search the item if it exists
        for i in range(0, len(customer), 4):
            if search == customer[i]:
                found = True  
                value = i  
                break  
            
        if found:
            print('Your Searched Customer Found!') 
            print("Customer_Name \t\t Customer_ID \t\t Custoemr_Address. \t\t Customer_City \t\t") 
            print(customer[value], '\t\t\t', customer[value + 1], '\t\t\t', customer[value + 2], '\t\t\t\t', customer[value + 3]) # display the Customer entities of the searched Customer
            customer_menu()
        else:
            print('Searched Customer not found')  
            customer_menu()  
    else:
        print('There is no Record of Customers to be Searched For')
        customer_menu()  
            
def delete_customer():
    if customer:
        found = False  
        q = input('Enter Name Customer you want to delete record for ') 
        for i in range(0, len(customer), 4):
            if q == customer[i]:
                found = True 
                value = i  
                break 
        if found:
            customer.pop(value + 3) 
            customer.pop(value + 2) 
            customer.pop(value + 1) 
            customer.pop(value) 
            print('Record of Customer having Sales Id: ', q, ' has been deleted')
            customer_menu() 
        else:
            print('The customer you searched for doesnot exist') 
            customer_menu2() 
    else:
        print('No Customer Record are there to be deleted') 
        customer_menu2()



def customer_menu():
    print('Press 1 to Add Customer \nPress 2 to View Customer \nPress 3 to Edit Customer \nPress 4 to Search Customer \nPress 5 to Delete Customer  \nPress 6 to Go back to main menu') # display the available functions 
    ask = int(input('Enter Corresponding Number to Perform Desired Task ')) 
    if ask == 1:
        print('Add Customers') 
        add_customer() 
    elif ask == 2:
        print('View Customers') 
        view_customer()
    elif ask == 3:
        print('Edit Customers')
        edit_customer()
    elif ask == 4:
        print('Search for Customers') 
        search_customer()
    elif ask == 5:
        print('Delete Customer') 
        delete_customer()
    elif ask == 6: # if user types 6
        menu() # exit the program
    else:
        print('Please enter a valid number') # tell the user that he has to enter valid number
        customer_menu()  # call the menu() function again to display the menu for user

def add_sale():
    confirm = "yes"
    while confirm == "yes":
        sale_ID = input("Enter sale ID for the bike: ")
        if sale_ID in sale:
            print("ID already alloted. Please try a different ID!")
            continue
        sale.append(sale_ID)
        sale.append(input("Enter dealer name: "))
        sale.append(input("Enter city: "))
        
        while True:
            sold_bike = input("Enter ID of bike to sale:")
            if sold_bike in bike:
                sale.append(sold_bike)
                break
            else:
                print("Enter The Correct ID of bike")
                continue
                
        while True:
            bike_customer = input("Enter ID of customer:")
            if bike_customer in customer:
                sale.append(bike_customer)
                break
            else:
                print("Enter The Correct ID of customer")
                continue
        confirm =input("Enter yes to repeat, no to exit: ")
        
def view_sale():
    print("SALE_ID\t\t\tDEALERSHIP\t\tDEALER CITY\t\tBIKE ID\t\t\tCUSTOMER ID")
    print(sale[0],"\t\t\t",sale[1],"\t\t\t",sale[2],"\t\t\t",sale[3],"\t\t\t",sale[4],)
    
def sales_menu():
    while True: # if condition satisfies then following runs  
        print('Press 1 to Add Sale\nPress 2 to view Sale\nPress 3 to Go back to main menu\nPress 4 to Exit')
        ask = eval(input('Enter Corresponding Number to Perform Desired Task:  ')) # ask user what function he wants to perform
        if ask == 1:
            add_sale()
        elif ask == 2:
            view_sale()
        elif ask == 3:
            menu()
        elif ask == 4:
            exit()
        else:
            print('Please enter a valid number') # tell the user that he has to enter valid number
            sales_menu()  # call the sales_menu() function again to display the menu for user

def menu():  # menu function definition
    while True: # if condition satisfies then following runs  
        print('Press 1 to Bike_Record \nPress 2 to Customer_ID \nPress 3 to Sale \nPress 4 to Exit') # display the functions user can perform
        ask = eval(input('Enter Corresponding Number to Perform Desired Task  ')) # ask user what function he wants to perform
        if ask == 1:  # if user types 1 
            print('Bike Record\n') # tell the user that he is going to add Customers
            bike_menu() # calls the add function
        elif ask == 2:
            print("\nCustomer_Record\n")
            customer_menu()
        elif ask == 3:
            print("Sale OF Bike\n")
            sales_menu()
            break
        else: # if user types something that was not expected
            print('Please enter a valid number') # tell the user that he has to enter valid number
            menu()  # call the menu() function again to display the menu for user
            
            
print('BIKE MANAGEMENT SYSTEM  ^_^ ') #display the heading
menu()