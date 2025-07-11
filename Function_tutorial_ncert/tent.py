"""Make programm to take dimensioins as
input from user & output length of fabric
required and total payable amount"""

#Taking input from the user---

print("Enter dimension of Tent(in meter):---")
h=float(input("Enter the height of tent:"))
r = float(input("Enter the radius of the tent:"))
s=float(input("Enter the slant height of tent:"))

#define Constant Pi=3.14
pi=3.14

#Curved Surface Area of conical part
csa_cone=pi*r*s

#Curved Surface Area of cyllinder part
csa_cyllinder=2*pi*r*h

#Total area of canvas--
Total_Area=csa_cone+csa_cyllinder

print("Total Area of canvas is- ",Total_Area)

#Dimension of fabric
w=float(input("Enter width of fabric:"))
l=(Total_Area/w)
print("Length of the fabric required:",l)
p=int(input("Enter price per meter lentgth of fabric:"))
Total_cost=(l*p)+118/100
print("The total cost to be paid(with 18 1percent GST):",Total_cost)
















