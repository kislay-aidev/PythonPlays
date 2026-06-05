n = int(input("Enter a number:"))
if n <= 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    print("Nth value in Fibonacci series is:", b if n>0 else a)