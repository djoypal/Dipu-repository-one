x= str(input("Enter a valid credit card number: "))
x=x.replace(" ","")
sum=0
ar=[]
l=len(x)
for i in range(0,l):
    ar.append(int(x[i]))

for i in range(l-2,-1,-2):
    ar[i]=ar[i]*2
    if(ar[i]>9):
        ar[i]=ar[i]-9
print("\n",ar)
for i in range(0,l):
    sum=sum+ar[i]
print("\n",sum)
if(sum%10==0):
    print("\nvalid")
else:
    print("\nInvalid")




