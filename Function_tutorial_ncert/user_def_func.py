"""Creation of userdefined Function"""

# def welcome_messege():
#     'Funtion to print a welcome messege'    #Docstring describing the function
#     print("Welcome to wonder world")   
    
    
# welcome_messege()  ## The fuction won't execute by itself , we need to call it whenever needed in code 
# print("Def of Function: ",welcome_messege.__doc__)  # we call the docstring here

def Add(a,b):            #presenting with argument
    c=a+b
    print(c)

Add(2,3)   # we call the function here and pass the value of a and b as 2 and 3


def Add (a,b):            #presenting with argument
    c=a+b
    return c          

c=Add(2,5)          #as we have used return statement in function so it will return the value to c and we can print it outside the function also 
print(c)          