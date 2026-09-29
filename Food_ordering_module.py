cart = []
items=["Burger","Pizza","Pasta","French fries"]

def add_items(choice):

    print(f"{items[choice-1]} has been added to cart.")
    cart.append(items[choice-1])

def remove_items(choice):

    print(f"{items[choice-1]} has been removed from cart.")
    cart.remove(items[choice-1])

def billing_discount(price):
    y=[]
    print("-"*75)
    print("Your final items and quantity are as follows: ")
    for i in cart :

        if i not in y :
            print(f"{i} x",cart.count(i) )
            y.append(i)
    expense = 0
    for i in y :

        expense += cart.count(i) * price[items.index(i)]
    print("-"*75)
    print("Your total expense is : ", expense)
    print("-"*75)       


    if expense >= 500 and expense < 1000 :
        print("YAY! You got a 5 percent discount. ")
        expense = expense - (5/100)*expense
        print("Your new total expense is : ", expense)
        print("-"*75)
    elif expense >= 1000:
        print("YAY! You got a 10 percent discount. ")
        expense = expense - (10/100)*expense
        print("Your new total expense is : ", expense)
        print("-"*75)
