# print star patten
print("How many rows you want to print")
n=int(input())
print("Type 1 if you want right angle triangle star pattern")
print("or type 0 if you want inverted right angle triangle star pattern")
b=bool(int(input()))
if (b==True):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*",end=" ")
        print()
elif (b==False):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*",end="")
        print()
           
 
    
        