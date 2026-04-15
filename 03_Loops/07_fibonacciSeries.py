# fibonacci series

n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    while count < n:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        count += 1 
        
# for i in range(n):
#     print(a, end=' ')
#     c = a + b
#     a = b
#     b = c 