"""Another way of doing this tent 
problem in organised Modular programming way using
Functions to enhance readibility and reuseability"""

from math import pi

#Curved surface area of cyllinder 
def cyllinder(h,r):
    area_cyl=2*pi*r*h
    return area_cyl
#Curved surface area of cone
def cone(l,r):
    area_con=pi*r*l
    return area_con
#Length of Fabric
def fabric_len(total_area,width_fabric):
    length=total_area/width_fabric
    return length
#Find cost exclusive of tax 
def cost(length_fabric,rate):
    total_cost=length_fabric*rate
    return total_cost
#Net amount inclusive of tax
def net_pay(cost):
    tax=0.18*cost 
    Net_price=cost+tax
    return Net_price




print("Enter dimension of Tent(in meter):---")
h=float(input("Enter the height of tent:"))
r = float(input("Enter the radius of the tent:"))
s=float(input("Enter the slant height of tent:"))
print("\n\n\n")

csa_cone=cone(s,r)
csa_cyllinder=cyllinder(h,r)
print(".............................")
Total_area=csa_cone+csa_cyllinder
print("Total area:",Total_area)

length_of_fabric=fabric_len(Total_area,20)
print("Length of fabric req:--",length_of_fabric)

rate=float(input("Please Enter the rate of the fabric :--"))
Total_cost_ex_Tax=cost(length_of_fabric,rate)

Total_cost_in_Tax=net_pay(Total_cost_ex_Tax)
print("Price exclusive of tax:",Total_cost_ex_Tax)
print("price inclusive of tax:",Total_cost_in_Tax)









