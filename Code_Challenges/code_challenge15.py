def code_challenge15():

    print("Good day, user!")
    isContinue = True
    num = 0
    while isContinue == True:
        question = input("Do you want to add another triangle? ( yes or no ): ")
        
        if question.lower() == "no":
            print("Loop is terminated")
            break
            
        elif question.lower() == "yes":
            num += 1
            for e in range(1,5):
                for x in range(1, num+1):
                    for s in range(1, e +1):
                        print("*", end=" ")
                    for m in range(5, e, -1):
                        print(" ", end=" ")
                print()
            continue
        else:
            print("Invalid answer, please only type 'yes' or 'no'. ")
            continue    
    