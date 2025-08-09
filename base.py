# user input 2 value and operator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

try:
    a = float(input("Enter the first value :"))
    op = input("Enter the operator :")
    b = float(input("Enter the second value :"))


    if(op=="+"):
        print(add(a,b))
    elif(op=="-"):
        print(sub(a,b))
    elif(op=="*"):
        print(mul(a,b))
    elif(op=="/"):
        print(div(a,b))
    else:
        print("Error: Invalid operator")
except ValueError:
    print("You didn't enter the values correctly")

