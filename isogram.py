x=str(input("Enter the string: "))
l=len(x)
s=0
for i in range(0,l):
    if(chr(32)<=(x[i]) and x[i]<=chr(47)):
        continue

    else:
        for j in range(i+1,l):
            if(x[i]==x[j]):
                s=s+1
                break
if(s==0):
    print("\n Isogram")
else:
    print("\n Nonisogram")

