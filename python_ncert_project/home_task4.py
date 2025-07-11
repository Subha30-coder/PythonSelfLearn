"""DETERMINE WHETHER A NUM IS PERFECT NUM / ARMSTRONG NUM / PALINDROME NUM"""

#CHECKING FOR PERFECT NUM----   #eg 6=> factors(1,2,3)=>if add factor will get 6

n=int(input("Enter the num n:"))
sum=0
for divisor in range(1,(n//2)+1):
    if (n%divisor)==0:
        sum+=divisor
if sum==n:
    print("It's a Perfect Num")
else:
    print("Not a Perfect num----")




#CHECKING FOR ARMSTRONG NUM---  # 153=> 1³ + 5³ + 3³==153, so extract each digit and qube them and add
    
C

quotient=n
sum=0
while quotient>0:
    reminder=quotient%10
    sum+=pow(reminder,3)
    quotient=quotient//10
if sum==n:
    print("Input is an Armstrong num:")
else:
    print("Input is not Armstrong---")
    



#CHECKING FOR PALLINDROME----

n=int(input("Enter your num n:"))
quotient=n
reverse=""
while quotient>0:
    remainder=quotient%10
    reverse+=str(remainder)
    quotient//=10
print("Your Pallindromic Seq is :",reverse)
