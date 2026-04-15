# Implicit Type Conversion
num1 = 10
num2 = 20.5
result = num1 + num2 # num1 is converted to float before addition
print("Result of Implicit Type Conversion:", result)


# Explicit Type Conversion (Casting)
num1 = 10
num2 = 20.5
result = num1 + int(num2) # num2 is explicitly converted to int before addition
print("Result of Explicit Type Conversion:", result)