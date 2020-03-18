print("GARIB DA DHABA")
print("1.Paneer         Rs.100 plate")
print("2.Matar Paneer   Rs.150 plate")
print("3.Dal Fry        Rs.100 plate")
print("4.Sahi Paneer    Rs.150 plate")
print("5.Bread          Rs.10  pice ")
ch=int(input("enter your choice (0-5) : "))
if ch== 1:
    price=100
elif ch==2:
    price=150
elif ch==3:
    price=100
elif ch==4:
    price=150
elif ch==5:
    price=10
else:
    print("wrong choice")
    price=0
pc=tuple()
q=tuple()
pr=tuple()
t=tuple()
size=int(input("enter your no of product to purchase"))
for c in range (0,size):
    pch=int(input("enter no product"))
    qty=     int(input("enter quantity"))
    price=float(input("enter your price"))
    total=price*qty
    pc=pc(pch,)
    q=q+(qty,)
    pr=pr(price,)
    t=t+(total,)

print ('no pro to pur           product          qty            price           total')
    

    
    
    
    

       

