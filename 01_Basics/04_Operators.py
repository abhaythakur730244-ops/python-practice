#Operators
#Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)        # 15
print("Subtraction:", a - b)     # 5
print("Multiplication:", a * b)  # 50
print("Division:", a / b)        # 2.0
print("Modulus:", a % b)         # 0
print("Exponentiation:", a ** b) # 100000

#Comparison Operators (Relational Operators)
print("Equal to:", a == b)       # False
print("Not equal to:", a != b)   # True
print("Greater than:", a > b)     # True
print("Less than:", a < b)        # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)     # False 

#Logical Operators
x = True
y = False
print("Logical AND:", x and y)    # False
print("Logical OR:", x or y)      # True
print("Logical NOT:", not x)      # False

#Assignment Operators
c = 10
c += 5  # c = c + 5
print("After += 5:", c)  # 15
c -= 3  # c = c - 3
print("After -= 3:", c)  # 12
c *= 2  # c = c * 2
print("After *= 2:", c)  # 24
c /= 4  # c = c / 4
print("After /= 4:", c)  # 6.0
c %= 5  # c = c % 5
print("After %= 5:", c)  # 1.0

#Bitwise Operators
p = 5  # In binary: 0101
q = 3  # In binary: 0011
print("Bitwise AND:", p & q)  # 1 (0001)
print("Bitwise OR:", p | q)   # 7 (0111)
print("Bitwise XOR:", p ^ q)  # 6 (0110)
print("Bitwise NOT:", ~p)      # -6 (in binary: 101
print("Left Shift:", p << 1)  # 10 (In binary: 1010)
print("Right Shift:", p >> 1) # 2 (In binary: 0010)