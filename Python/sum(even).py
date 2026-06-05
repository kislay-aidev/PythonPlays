#1-n even numbers sum
n = int(input("Enter the number:"))
sum = 0

for i in range (0, n+1, 2):
    sum += i
print("Sum of N natural even numbers betweer 1 and N are: ", sum)