

print("a^2 = x (mod p)")
p = int(input("enter p value:"))

x = int(input("enter x value:"))

for a in range(p-1):
    b = (a*a)%p
    if b == x:
        print("x is a quadratic residue ")
        print("for a value : ",a)
    else:
        continue

    



