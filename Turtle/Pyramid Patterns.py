rows = 5
print("Half Pyramid: ")
for i in range (1, rows+1):
    print('*'*i)
    
print("\nInverted half Pyramid: ")
for i in range (rows, 0, -1):
    print('*' * i)
    
print("\nFull pyramid: ")
for i in range (rows):
    print(' ' * (rows-i-1) + '* ' * (i+1))