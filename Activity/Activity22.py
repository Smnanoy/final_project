def act22():

    def act1():
        print("hello world")

    def act2():
        name= input("please enter your name:")
        print("Hi" + name)

    def act3():
      
      fullname = input("please input your full name:")
      City = input("please input your city:")
      Province = input("please input your province:")
      Postal_code = input("please input the postal code of the province:")
      Cellphonenumber = input("please input your cellphone number:")
      Email = input("please input your email:")
      Birthday = input("please input you birhday:")
      BirthPlace = input("please input your birth place:")
      Age = input("please input your age:")
      CivilStatus = input("please input your civil status:")
      Height = input("please input your height in ft:")
      Weight = input("please input your weight in kg:")
      Religion = input("please input your religion:")
      Gender = input("please input your gender:")
      Citezenship = input("please input your cintezenship:")
      FatherName = input("please input your father's name:")
      SiblingName = input("please input your sibling's name:")
      print("My name is:" + fullname + 
            "\nI'm from the city of:" + City + 
            "\nI'm from the province of:" + Province + 
            "\nThe postal code of:" + Province + ",is the:" + Postal_code + 
            "\nMy cellphone number is:" + Cellphonenumber + 
            "\nMy Email is:" + Email + 
            "\nMy Birthday is:" + Birthday + 
            "\nMy Birth Place:" + BirthPlace + 
            "\nMy age is:" + Age + 
            "\nMy civil status is:" + CivilStatus +
            "\nMy height in Ft is:" + Height + 
            "\nMy weight in kilogram is:" + Weight + 
            "\nMy religion is:" + Religion + 
            "\nMy gender:" +Gender + 
            "\nMy citezenship is" + Citezenship + 
            "\nMy Father's full name is:" + FatherName + 
            "\nMy sibling's full name is:" + SiblingName + 
            "\nThis is my BIONOTE")

    def act4():
        number1= input("enter a numbe:")
        number2= input("enter a number:")
        answer= number1 + number2
        print("The sum of:",number1 + " + " +number2 + " is " + answer)

    def act6():
        x = 5
        print(x)
        x =  x + 10
        print(x)
        x =  x + 15
        print(x)

    def act7():
        gold=0
        miner= input("Hi, what is ypour name:")
        isgold= input("is the mineral gold?")

        if isgold == "yes":
            gold+=1 
            print(f" Hi {miner}, Your total number of gold is {gold}")
        else:
            print(f"INVALID")
    
    def act8():
        password= input("enter your password: ")
        if password. lower() == "secret":
            print(" Access Granted")
            print(" Enjoy using the System")
        elif password. lower() == "maspogikaysir12":
            print(" Enjoy using the System")
        else:
            print(" access denied")

    def act9():
        age= eval(input ("Please enter your age:"))
        if age>=1 and age <=7:
            print("toddler")
        elif age>=8 and age <=13:
            print("your age is considered as Pre teen")
        elif age >=14 and age <= 18:
            print("your age is considered as Teenager")
        elif age >=19 and age <= 31:
            print("your age is considered as Early Adulthood ")
        elif age >= 32 and age <= 45:
            print("your age is considered as Mid adulthood")
        elif age >= 46 and age <=59:
            print("your age is considered as Post Adulthood")
        elif age >=60:
            print("your age is considered as Senior")

    def act10():
        name = input(" please enter your name:  ")
        isstudent = input(" are you a student of DLL:  ")

        if isstudent.lower() == "yes":
            yearlevel = input("what year are you currently enrolled?",
            "\nf- freshman \ns- sophomore \nr- senior:",
            "\n please enter your grade level:  ")
            
            if yearlevel.lower() == "f":
                print(f" hi {name}, freshman, welcome to DLL")
            
            elif  yearlevel.lower() == "s":
                print(f" hi {name}, senior, welcome to DLL")
        else:
            print("thank you for using the system")
            
    def act11():
        for ulit in range(1 , 10):
            print("akin ka na lang ulit")
                                                                                                                                                                                                
    def act12():
        for x in range(10,1):
            print("akin lang ikaw")

    def act13():
        num = int(input("enter a number: "))
        for x in range(num , 0, -1):
            x()
            print(x)
    
    def act14():
        for x in range(0,11):
            print(x, end= "-")
            for y in range(0,11):
                print("*", end ="")
            print()

    def act15():
        for x in range(0,11):
            print(x, end= " ")
            for y in range(0,x):
                print("*", end =" ")
            print()

    def act16():
            for x in range(1, 11):
                for z in range(1, x + 1):
                    print(" ", end=" ")
                for y in range(11, x, -1):
                    print("*", end= " ")

                print()

    def act17():
        column= eval(input("enter a number--->"))
        for x in range(1,11):
            for y in  range(1, column + 1):
                print(f"{x} x {y} = {x * y}", end= "\t")
            print()

    def act18():

        nt= eval(input("enter a number--->"))
        for x in range (1,5):
            for r in range(1, nt + 1):
                for y in range(1, x +1):
                    print("*", end= " ")
                for z in range(5, x, -1):
                    print(" ", end= " ")
                print(end = " ")
            print()
    
    def act19():

        import imp
        import os
        isContinue = True
        no=0
        while isContinue == True:
            ask = input("whould you like to add another triangle (yes / no) -->")
            if ask.lower() == "no":
                print("PROGRAM TERMINATED")
                break
                isContinue = False
            else:
                os.system('cls')
                no +=1

act22()

            



                





                                                                                                                                                                                                                    