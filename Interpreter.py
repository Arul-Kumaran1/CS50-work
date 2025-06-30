a = input("Expression: ")
b, operator, y = a.split()
b = int(b)
y = int(y)
result = None
if operator == '+':
     result = b + y
elif operator == '-':
     result = b - y
elif operator == '*':
     result = b * y
elif operator == '/':
    result = b/y
print(f"{result:.1f}")