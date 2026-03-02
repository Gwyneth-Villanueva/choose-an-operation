n1 = float(input("Enter first number: "))
op = input("Choose an operation (+ - * /): ")
n2 = float(input("Enter second number: "))

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2 if n2 != 0 else "Cannot divide by zero")
else:
    print("Invalid operation")

