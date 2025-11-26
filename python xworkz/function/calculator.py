def userinput():
    first_input=int(input("enter the first number: "))
    second_input=int(input("enter the second number: "))
    return first_input,second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b
def mul(a=0,b=0):
    return a*b
def div(a=0,b=1):
    return a/b
print("welcome to calculator")
while True:
    print("select the choose:\n 1:add\n 2:sub\n 3:mul\n 4:div")
    choose=int(input("enter the choose:"))
    if choose==1:
        x,y=userinput()
        print("addition of number",add(x,y))

    elif choose==2:
        x,y=userinput()
        print("subtratction of number", sub(x, y))
    elif(choose==3):
        x,y=userinput()
        print("multiple of number",mul(x,y))
    elif(choose==4):
        x,y=userinput()
        print("divide of number", div(x, y))
