def code_challenge10():

  for j in range (1,6):
    for k in range(6, j, -1):
      print(" ",end="  ")
    for e in range (1, j+1):
      print("*", end="  ")
    for n in range (1, j+1):
      print ("*", end="  ")
      
    print()
    
  for a in range(1,5):
    for b in range(1, a+2):
      print(" ", end="  ")
    for q in range(5, a, -1):
      print("*", end="  ")
    for w in range (5, a, -1):
      print ("*", end="  ")
      
    print()