def code_challenge13():

    #upper part of the diamond
    for i in range(1, 5 + 1):
    
        for j in range(5 - i):
            print("  ", end="  ")
            
        for j in range(i, 0, -1):
            print(j, end="  ")
            
        for j in range(2, i + 1):
            print(j, end="  ")
        print()

    # down part of the diamond
    for i in range(5 - 1, 0, -1):
    
        for j in range(5 - i):
            print("    ", end=" ")
            
        for j in range(i, 0, -1):
            print(j, end="  ")
            
        for j in range(2, i + 1):
            print(j, end="  ")
        print()
