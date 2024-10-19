n1 = int(input("Enter the first number : "))
sym = str(input("+ - * /"))
n2 = int(input("Enter the second number:"))

if sym == "+":
    print(n1 + n2)

elif sym == "-":
    print(n1 - n2 )

elif sym == "*":
    print(n1 * n2)

elif sym == "/":
    print(n1 / n2)
else:
    print(" Error Enter the numbers!")