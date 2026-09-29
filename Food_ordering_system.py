from Food_ordering_module import *


print("VITB RESTAURANT")
print("-"*75)
print("======   MENU   ======\n" "1. Burger       120\n" "2. Pizza        250\n" "3. Pasta        180\n" "4. French fries 100" )
print("-"*75)

items=["Burger","Pizza","Pasta","French fries"]
no_of_items = int(input("Enter the number of items you want to order: "))
price = [120,250,180,100]

while no_of_items > 0 :
    print("-"*75)
    choice = int(input("Enter what you want to order: "))
    print("-"*75)

    if choice==1:
        add_items(choice)

    elif choice==2:
        add_items(choice)

    elif choice==3:
        add_items(choice)

    elif choice==4:
        add_items(choice)

    no_of_items -= 1

print("-"*75)
print_cart = input("Do you want to see the items you added to cart? (y/n): ")
print("-"*75)

if print_cart == "y":
    print(cart)

print("-"*75)
final = input("Before finalising your order , do you want to remove or add any food items?(y/n): ")
print("-"*75)

i = 1

while i == 1 :

    if final == "y":
        print("-"*75)
        edit_add = input("Do you want to add food items? (y/n): ")
        print("-"*75)

        if edit_add == "y":
            print("-"*75)
            new_add = int(input("Enter what you want to order: "))
            print("-"*75)

            if new_add==1:
                add_items(new_add)

            elif new_add==2:
                add_items(new_add)

            elif new_add==3:
                add_items(new_add)

            elif new_add==4:
                add_items(new_add)
        print("-"*75)
        edit_remove = input("Do you want to remove food items? (y/n): ")
        print("-"*75)
        if edit_remove =="y": 
            print("-"*75)
            new_remove = int(input("Enter what you want to remove : "))
            print("-"*75)

            if new_remove ==1:
                remove_items(new_remove)

            elif new_remove ==2:
                remove_items(new_remove)

            elif new_remove ==3:
                remove_items(new_remove)

            elif new_remove ==4:
                
                remove_items(new_remove)
    print("-"*75)
    i = int(input("Before finalising your order , do you want to remove or add any food items again? ( Enter 1 to continue, 0 to) :"))
    print("-"*75)


billing_discount(price)


