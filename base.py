# food ordering system
# first it will show a menu with available foods and their prices
# user input which foods and drinks they will order
# the total cost will be then displayed with 2% VAT 
# and then prompt user to give tips or not
# then will show the final cost including foods ordered (optional)

print("Welcome to Shantor Goriber Restaurant\n")
print("Menu :\n")

menu = ["0# Pizza = 2$" , "1# Burger = 3$" , "2# Chowmin = 4$" , "3# coke = 1$" , "4# Orange Juice = 1$\n" ]

for i in menu :
    print(i)

print("To Choose your orders press corresponding numbers in pos :\n ")

isconfirm = 0
bill = 0
order = []

while(isconfirm == 0):


    pos = input("To finalize your order press y") 
    

    if(pos=="0"):
        order.append("Pizza        = 2$")
        bill += 2
    elif(pos=="1"):
        order.append("Burger       = 3$")
        bill += 3
    elif(pos=="2"):
        order.append("Chowmin      = 4$")
        bill += 4
    elif(pos=="3"):
        order.append("coke         = 1$")
        bill += 1
    elif(pos=="4"):
        order.append("Orange Juice = 1$")
        bill += 1
    elif(pos=="y"):
        isconfirm = 1
    else:
        print("Invalid Input")
        isconfirm = 1

vat = bill*(2/100)

print("Recipt :\n")
for i in order:
    print(i)

print("\n")
print("------------------------------")
print(f"Subtotal = {bill}")
print(f"VAT (2%) = {vat}")
tips=0
prompt=input("Would you like to leave us a tip (y/n)")
if(prompt=="y"):
    tips = int(input("Add the amount of tips"))
    print(f"Tips     = {tips}")
    print(f"Total    = {bill + tips + vat}\n")
else:
    print(f"Total    = {bill + tips + vat}\n")
print("Thank you for your Purchase !")