def code_challenge12():
    # arrowhead
    for j in range(1, 6):
        for k in range(j, 6):
            print(" ", end=" ")
        for e in range(1, j + 1):
            print("*", end=" ")
        for n in range(1, j):
            print("*", end=" ")
        print()

    # Lower part of the arrow 
    for i in range(0, 5):
        for j in range(1, 6):
            print(" ", end=" ")
        print("* *") 

