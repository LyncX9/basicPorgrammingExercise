def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y) 

def divide(x,y):
    return(x/y)

no1=eval(input("Enter First Number:"))
no2=eval(input("Enter Second Number:"))

print("Select The   Option:")
print("1. Addition")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while(True):
    choice=int(input("Enter the choice from 1,2,3,4,5: "))
    if choice in (1,2,3,4,5):
        if choice==1:
            print(no1,"+",no2,"=",add(no1,no2))
            
        elif choice==2:
            print(no1,"-",no2,"=",subtract(no1,no2))
            
        elif choice==3:
            print(no1,"*",no2,"=",multiply (no1,no2))
            
        elif choice==4:
            print(no1,"/",no2,"=",divide(no1,no2))
        elif choice==5:
                print("Thank You: ")
                exit()
    else:
        print("Invalid Choice Try Agai:")            