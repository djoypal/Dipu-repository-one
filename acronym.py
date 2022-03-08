x=str(input("Enter the string: "))
l=len(x)
print("\n",x[0],end="")
for i in range(0,l):
    if(x[i]==" "):
        print(x[i+1],end="")


