"""Another way of doing this tent 
problem in organised Modular programming way using
Functions to enhance readibility and reuseability"""

from math import pi


def cyllinder(h,r):
    "Curved surface area of cyllinder "
    area_cyl=2*pi*r*h
    return area_cyl

def cone(l,r):
    "Curved surface area of cone"
    area_con=pi*r*l
    return area_con

def fabric_len(total_area,width_fabric):
    "Length of Fabric"
    length=total_area/width_fabric
    return length
 
def cost(length_fabric,rate):
    "Find cost exclusive of tax"
    total_cost=length_fabric*rate
    return total_cost

def net_pay(cost):
    "Net amount inclusive of tax"
    tax=0.18*cost 
    Net_price=cost+tax
    return Net_price

## The fuction won't execute by itself , 
# we need to call it whenever needed in code.



print("Enter dimension of Tent(in meter):---")
h=float(input("Enter the height of tent:"))
r = float(input("Enter the radius of the tent:"))
s=float(input("Enter the slant height of tent:"))
print("\n\n\n")

csa_cone=cone(s,r)                    #here we call the function cone that had made before
csa_cyllinder=cyllinder(h,r)            # here we call the function cyllinder
print(".............................") 
Total_area=csa_cone+csa_cyllinder
print("Total area:",Total_area)

length_of_fabric=fabric_len(Total_area,20)    #here we call the function  fabric_length
print("Length of fabric req:--",length_of_fabric)

rate=float(input("Please Enter the rate of the fabric :--"))
Total_cost_ex_Tax=cost(length_of_fabric,rate)                 # we call the function cost

Total_cost_in_Tax=net_pay(Total_cost_ex_Tax)                   #we call the fuction net_pay
print("Price exclusive of tax:",Total_cost_ex_Tax)
print("price inclusive of tax:",Total_cost_in_Tax)









