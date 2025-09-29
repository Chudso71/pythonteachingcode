# [ ] create fucntion, call and test 
def cheese(order_amount, max=30,min=3,price=34,):
    int(max)
    int(min)
    int(price)
    int(order_amount)
    if int(order_amount) > 30:
        print(order_amount, "is above maximum order amount")
    elif int(order_amount) < 3:
        print(order_amount, "is below minimum order amount")
    else:
        return(float(order_amount), "costs" ,int(order_amount) * int(price))
weight = input("Cj Hudson, enter cheese order weight (numeric value):")

print(cheese(weight))