# [ ] create, call and test the adding_report() function
#function
def adding_report(A):
    print("Input an integer to add to the total or \"Q\" to quit:")
    items = ""
    T = 0
    while True:
        hold = input("Enter an integer or \"Q\"")
        if hold.lower() == "q":
            break
                  
        elif hold.isdigit():
            T += int(hold)
            if A.upper() == "A":
                items += hold + "\n"
                #store inputs for items list
            
        else:
            print(hold + " is invalid input")
    
    if A.upper() == "A":
        print("Items")
        print(items)
        #used to make items list and print values

    return T

        
A = "A" 
Total = adding_report(A)
#Used to call function and Total value
print("\nTotal\n",Total, "\n Calculated by: [Cj Hudson]")



