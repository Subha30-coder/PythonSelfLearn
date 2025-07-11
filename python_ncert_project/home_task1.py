"""Input two numbers and display the larger/smaller"""
a=float(input("Enter num 1st:"))     ## method 1
b=float(input("Enter num 2nd:"))
if a<b:
    print("the smaller num is:",a)
    print("the larger num is:",b)
elif a==b:
    print(a,"is equals to",b,sep=" ")
else:
    print("the smaller num is:",b)
    print("the larger num is:",a)
    
# method 2

a=float(input("Enter num 1st:"))      
b=float(input("Enter num 2nd:"))
greater=None                              #we need to predefine greater and smaller is none if inputs were equals
smaller=None
if a<b:
    greater=b
    smaller=a
elif a>b:
    greater=a
    smaller=b
else :
     print(a,"is equals to",b,sep=" ")
print(greater,"is greater num",sep=" ")
# print(smaller,"is smaller num",sep=" ")




"""Input three numbers and display the largest/smallest"""

a=float(input("Enter the 1st number:"))
b=float(input("Enter the 2nd number:"))
c=float(input("Enter the 3rd number:"))
if (a==b) and (b==c):
    print("All are equal",a,b,c,sep=" = ")            # to avoid the error of greatest smallest while hitting equal input 
else :    
    if (a>b) and (a>c):                             #we just whole indent the statemnt of paragraph after first under first else selecting all+ tab press
        greatest=a
        if b>c:smallest=c
        else:smallest=b                           # here we use the and function , if both true then truthval true
    elif (b>c) and (b>a):
        greatest=b
        if c>a:smallest=a
        else:smallest=c
    else:
        greatest=c
        if a>b:smallest=b
        else:smallest=a
    print("\n\n\n")
    print("Result out of the three numbers :",a,b,c,sep=" ; ")
    print(greatest,"is greatest")
    print(smallest,"is smallest")




















           
           
           

