def gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

number1 = int(input("first number:"))
number2 = int(input("second number:"))

print("here is their gcd:",gcd(number1,number2))

