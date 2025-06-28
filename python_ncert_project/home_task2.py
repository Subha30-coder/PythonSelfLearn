"""Make some pattern row(|) by column(-)"""  

"""for that specific pattern of  this type """  
# for row in range(1,6):              # *
#     for column in range(row):       # * *
#          print("*",end=" ")         # * * *
#     print("\n")                     # * * * *                                                                       
                                      # * * * * * 
                                      
# # for any general pattern as input(n)  of this type 
# n=int(input("enter value of n :"))
# for row in range(1,n+1):
#     for column in range(row):
#         print("*",end=" ")
#     print("\n")


""" for that specific pattern of  this type"""
# for row in range(1,6):  #row srart from 1,as set up                      # 1 2 3 4 5
#     for column in range(6-row):   # column starts from 0, by default     # 1 2 3 4
#         print(column+1,end=" ")                                          # 1 2 3
#     print("\n")                                                          # 1 2
#                                                                          # 1
           
# # for any general pattern as input(n)  of this type 
# n=int(input("enter the value n :"))
# for row in range(1,n+1):
#     for column in range((n+1)-row):
#         print(column+1,end=" ")
#     print("\n")     
           

""" for that specific pattern of  this type"""                                 #A
# for row in range(1,6):           #row range start from 1,as set                #A B
#     for column in range(row):     #column range starts from 0,by default       #A B C
#         print( chr(column+65),end=" ")  # chr()-->ASCIcode reader,chr(65)=A    #A B C D
#     print("\n")                                                                #A B C D E

# # for any general pattern as input(n)  of this type
# n=int(input("put the value n:"))
# for row in range(1,n+1):
#     for column in range(row):
#         print(chr(column+65),end=" ")
#     print("\n")

