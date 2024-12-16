def code_challenge8():

    print("Good day!")
    sum = 0
    odd = 0
    even = 0

    for x in range(1,11):
        num = eval(input(f"Enter #{x}:  "))
        sum += num
        
    for y in range(1,11):
            if y % 2 == 0:
                odd += y
                
            else:
                 even += y
            
    print(f"The sum of all numbers given is {sum}")
    print(f"The sum of all EVEN numbers is: {even}")           
    print(f"The sum of all ODD numbers is: {odd}")           
                        
                
                