#--------------------------------------------------------------------------------------------------------------------------
#Student Name: Jenesis
#Course: CIT 134A
#Term/Year: Fall 2022
#Date: 11/21/2022
#Project Number: 4
#--------------------------------------------------------------------------------------------------------------------------

# Display title
def display_title():
    print("Product Sales Management Systems")
    print()
    
# Display menu    
def display_menu():
    print("COMMAND MENU")
    print("view - View a sales amount for a specified month")
    print("highest - View the highest sales of the year")
    print("lowest - View the lowest sales of the year")
    print("edit - Edit a sales amount for a specified month")
    print("average - View the sales average for the whole year")
    print("range - View the sales average for a specified sales amount range")
    print("total - View the sales total for a whole year")
    print("exit - Exit a program")
    
def read_file(d):
    with open("monthly_sales.txt") as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val
        
def view_sales_amount(sales):
    month = input("Three-letter month: ")
    print (sales[month])
        
def get_highest_amount(sales):
    max_value = max(sales, key=sales.get)
    print(max_value,": ",sales[max_value])
    
def get_lowest_amount(sales):
    min_value = min(sales, key=sales.get)
    print(min_value,": ",sales[min_value])
    
def edit_sales_amount(sales):
    month = input("Three-letter month: ")
    salesInMonth = int(input("Enter sales: "))
    sales[month] = salesInMonth
    
def get_average(sales):
    salesSum = 0
    count = 0
    for i in sales.values():
        salesSum += i
        count += 1
    avg = salesSum / count 
    print(avg)
    
def get_range_average(sales):
    low = int(input("low: "))
    high = int(input("high: "))
    salesSum = 0
    count = 0
    for i in sales.values():
        if i >= low and i <= high:
            salesSum += i
            count += 1
    avg = salesSum / count 
    print(avg)
    
def get_total(sales):
    salesSum = 0
    for i in sales.values():
        salesSum += i
    print(salesSum)
    
def terminate_app():
    print("Thank you for using my app!")
     
# Main List
def main ():
    # The monthly_sales.txt in Dictionary form
    monthly_sales = {}
    read_file(monthly_sales)
    # Functions for the menu
    display_title()
    display_menu()
    command = input("Command: ")
    
    while command != "exit":
        if command == "view":
            # Display sales for ONE specific month
            view_sales_amount(monthly_sales)
        elif command == "highest":
            # Display highest sale of the year
            get_highest_amount(monthly_sales)
        elif command == "lowest":
            # Display lowest sale of the year
            get_lowest_amount(monthly_sales)
        elif command == "edit":
            # Edit a sales amount for specific month
            edit_sales_amount(monthly_sales)
        elif command == "average":
            # Average of sales for the whole year
            get_average(monthly_sales)
        elif command == "range":
            # Sales average for a specific sales amount range
            get_range_average(monthly_sales)
        elif command == "total":
            # Sales total for WHOLE year
           get_total(monthly_sales)
        else:
            print("Invalid command. Try again.")
            
        print()
        display_menu()
        command = input("Command: ")
        
    terminate_app()
    
main()



