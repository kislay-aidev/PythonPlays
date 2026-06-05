def butterfly():
    n = 5
    
    #upper half
    for i in range (1, n+1):
        #1st part stars
        for j in range (1, i+1):
            print("*", end = " ")
            i )
        #spaces
        spaces = 2*(n-i)
        for k in range (1, spaces+1):
            print(" ", end = " ")
            
        #2nd part stars
        for l in range (1, i+1):
            print("*", end = " ")
        print()
        
    #lower half
    for a in range (n, 0, -1):
        #1st part stars
        for b in range (1, a+1):
            print("*", end = " ")
            
        #spaces
        spaces = 2*(n-a)
        for c in range (1, spaces+1):
            print(" ", end = " ")
            
        #2nd part stars
        for d in range (1, a+1):
            print("*", end = " ")
        print()
        
butterfly()