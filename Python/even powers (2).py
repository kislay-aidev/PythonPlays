n = int(input("Enter number of even powers to display:"))

print("Even powers of 2:")
for i in range (0, n*2, 2):
    print(f"2^{i} = {2**i}")