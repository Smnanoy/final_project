"""Unfinished Project"""

import os

from Activity import ( activity1, activity2, activity3,activity4, activity5, 
                      activity6, activity7, activity8, activity9, activity10,
                      activity11, activity12, activity13, activity14, activity15,
                      activity16, activity17, activity18, activity19, activity20,
                      activity21, activity22, activity23, activity24, activity25
                      )

from Code_Challenges import( code_challange1, code_challange2, code_challenge4, code_challenge5,
                            code_challenge6, code_challenge7, code_challenge8, code_challenge9, code_challenge10, 
                            code_challenge11, code_challenge12, code_challenge13, code_challenge14, code_challenge15,
                            code_challenge16
                            )

def Clear():
    os.system("cls")

def Main_Menu():
    while True:
        try:
            print("\n\n\t--------------FINAL PROJECT-----------------"
                     "\n\t--------------<MAIN MENU>------------------"
                     "\n\t-------------------------------------------"
                     "\n\t1. Fundamentals \n\t2. Activities \n\t3. Code Challenges \n\t0. Exit "
            )
            ask = int(input("Enter the number of your choice: "))

            if ask == 1:
                Clear()
                Py_Fundamentals()
                continue
            elif ask == 2:
                Clear()
                Activity()
                continue
            elif ask == 3:
                Clear()
                Code_Challenges()
                continue

            elif ask == 0:
                Clear()
                choice = input("\n\n\tThe Final Project Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()
                
                if choice == "YES":
                    Clear()
                    print("\n\tThe Final Project will be terminated.")
                    break

                elif choice == "NO":
                    Clear()
                    print("\n\tThe Final Project will now continue.")
                    continue

            elif ask < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif ask >= 5:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Wrong Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue

def Activity():
    while True:
        try:
            print("\n\n\t-----------------------------------------------------------------------------------------"
                     "\n\t--------------------------------<Activities Menu>----------------------------------------"
                     "\n\t-----------------------------------------------------------------------------------------"
                     "\n\t1.Activity1 \n\t2.Activity2 \n\t3.Activity3 \n\t4.Activity4 \n\t5.Activity5 "
                     "\n\t6.Activity6 \n\t7.Activity7 \n\t8.Activity8 \n\t9.Activity9 \n\t10.Activity10 "
                     "\n\t11.Activity11 \n\t12.Activity12 \n\t13.Activity13 \n\t14.Activity14 \n\t15.Activity15 "
                     "\n\t16.Activity16 \n\t17.Activity17 \n\t18.Activity18 \n\t19.Activity19 \n\t20.Activity20 "
                    "\n\t21.Activity21 \n\t22.Activity22 \n\t23.Activity23 \n\t24.Activity24 \n\t25.Activity25 \n\t0.Return to Main Menu "
                     
            )
            num_act = int(input("Enter the number of your choice: "))

            if num_act == 1:
                Clear()
                activity1.act1()
                continue
            elif num_act == 2:
                Clear()
                activity2.act2()
                continue
            elif num_act == 3:
                Clear()
                activity3.act3()
                continue
            elif num_act == 4:
                Clear()
                activity4.act4()
                continue
            elif num_act == 5:
                Clear()
                activity5.act5()
                continue
            elif num_act == 6:
                Clear()
                activity6.act6()
                continue
            elif num_act == 7:
                Clear()
                activity7.act7()
                continue
            elif num_act == 8:
                Clear()
                activity8.act8()
                continue
            elif num_act == 9:
                Clear()
                activity9.act9()
                continue
            elif num_act == 10:
                Clear()
                activity10.act10()
                continue
            elif num_act == 11:
                Clear()
                activity11.act11()
                continue
            elif num_act == 12:
                Clear()
                activity12.act12()
                continue
            elif num_act == 13:
                Clear()
                activity13.act13()
                continue
            elif num_act == 14:
                Clear()
                activity14.act14()
                continue
            elif num_act == 15:
                Clear()
                activity15.act15()
                continue
            elif num_act == 16:
                Clear()
                activity16.act16()
                continue
            elif num_act == 17:
                Clear()
                activity17.act17()
                continue
            elif num_act == 18:
                Clear()
                activity18.act18()
                continue
            elif num_act == 19:
                Clear()
                activity19.act19()
                continue
            elif num_act == 20:
                Clear()
                activity20.act20()
                continue
            elif num_act == 21:
                Clear()
                activity21.act21()
                continue
            elif num_act == 22:
                Clear()
                activity22.act22()
                continue
            elif num_act == 23:
                Clear()
                activity23.act23()
                continue
            elif num_act == 24:
                Clear()
                activity24.act24()
                continue
            elif num_act == 25:
                Clear()
                activity25.act25()
                continue

            
            elif num_act == 0:
                Clear()
                choice_act = input("\n\n\tThe Activities Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()
                
                if choice_act == "YES":
                    Clear()
                    print("\n\tThe Activities Menu will now be terminated.")
                    break

                elif choice_act == "NO":
                    Clear()
                    print("\n\tThe Activities Menu will now continue.")
                    continue

            elif choice_act < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif choice_act >= 27:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Invalid Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue

def Code_Challenges():
    while True:
        try:
            print("\n\n\t-----------------------------------------------------------------------------------------"
                     "\n\t--------------------------------<Code Challenges Menu------------------------------------"
                     "\n\t-----------------------------------------------------------------------------------------"
                     "\n\t1.Code Challenge1 \n\t2.Code Challenge2 \n\t3.Code Challenge3 \n\t4.Code Challenge4\n\t5.Code Challenge5 "
                     "\n\t6.Code Challenge6 \n\t7.Code Challenge7 \n\t8.Code Challenge8 \n\t9.Code Challenge9 \n\t10.Code Challenge10 "
                     "\n\t11.Code Challenge11 \n\t12.Code Challenge12 \n\t13.Code Challenge13 \n\t14.Code Challenge14 \n\t15.Code Challenge15 "
                     "\n\t16.Code Challenge16 \n\t0.Return to Main Menu "
            )
            num_cc = int(input("Enter the number of your choice: "))

            if num_cc == 1:
                Clear()
                code_challange1.code_challenge1()
                continue
            elif num_cc == 2:
                Clear()
                code_challange2.code_challenge2()
                continue
            elif num_cc == 3:
                Clear()
                code_challenge13.code_challenge3()
                continue
            elif num_cc == 4:
                Clear()
                code_challenge4.code_challenge4()
                continue
            elif num_cc == 5:
                Clear()
                code_challenge5.code_challenge5()
                continue
            elif num_cc == 6:
                Clear()
                code_challenge6.code_challenge6()
                continue
            elif num_cc == 7:
                Clear()
                code_challenge7.code_challenge7()
                continue
            elif num_cc == 8:
                Clear()
                code_challenge8.code_challenge8()
            elif num_cc == 9:
                Clear()
                code_challenge9.code_challenge9()
                continue
            elif num_cc == 10:
                Clear()
                code_challenge10.code_challenge10()
                continue
            elif num_cc == 11:
                Clear()
                code_challenge11.code_challenge11()
                continue
            elif num_cc == 12:
                Clear()
                code_challenge12.code_challenge12()
                continue
            elif num_cc == 13:
                Clear()
                code_challenge13.code_challenge13()
                continue
            elif num_cc == 14:
                Clear()
                code_challenge14.code_challenge14()
                continue
            elif num_cc == 15:
                Clear()
                code_challenge15.code_challenge15()
                continue
            elif num_cc == 16:
                Clear()
                code_challenge16.code_challenge16()
                continue
    
            elif num_cc == 0:
                Clear()
                choice_cc = input("\n\n\tThe Code Challenges Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()

                if choice_cc == "YES":
                    Clear()
                    print("\n\tThe folder for Code Challenges will mow be terminated.")
                    break

                elif choice_cc == "NO":
                    Clear()
                    print("\n\tThe folder for Code Challenges will now continue.")
                    continue

            elif choice_cc < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif choice_cc >= 17:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Invalid Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue


def Py_Fundamentals():
    while True:
        try:
            print("\n\n\t-----------------------------------------------------------------------------------------"
                     "\n\t-----------------------------<Python Fundamentals Menu>----------------------------------"
                     "\n\t-----------------------------------------------------------------------------------------"
                     "\n\t1. Print Statements \n\t2. Variables \n\t3. Loops \n\t4. Operations \n\t5. Conditional "
                     "\n\t6. List \n\t7.Functions \n\t8.Return to Main Menu "
            )
            num_py_funda = int(input("Enter the number of your choice: "))

            if num_py_funda == 1:
                Clear()
                Print()
                continue
            elif num_py_funda == 2:
                Clear()
                Var()
                continue
            elif num_py_funda == 3:
                Clear()
                Loops()
                continue
            elif num_py_funda == 4:
                Clear()
                Opera()
                continue
            elif num_py_funda == 5:
                Clear()
                Condi()
                continue
            elif num_py_funda == 6:
                Clear()
                List
                continue
            elif num_py_funda == 7:
                Clear()
                Func()
                continue
           
    
            elif num_py_funda == 0:
                Clear()
                num_py_funda = input("\n\n\tThe Python Fundamentals Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()

                if num_py_funda == "YES":
                    Clear()
                    print("\n\tThe Python Fundamentals Menu will mow be terminated.")
                    break

                elif num_py_funda == "NO":
                    Clear()
                    print("\n\tThe folder for Python Fundamentals Menu will now continue.")
                    continue

            elif num_py_funda < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif num_py_funda >= 4:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Invalid Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue

def Print():
    while True:
        try:
            print("\n\n\t-----------------------------------------------------------------------------------------"
                     "\n\t----------------------------<Printing In Python Menu>----------------------------------"
                     "\n\t----------------------------------------------------------------------------------------"
                     "\n\t1.Definition \n\t2.Examples \n\t0.Return to Main Menu "
            )
            num_fun1 = int(input("Enter the number of your choice:"))

            if num_fun1 == 1:
                print( "\n\n\tThe print() function takes one or more arguments, which are converted"
                "\n\t into strings and then written to the console, followed by a newline character" 
                "\n\t(moving the cursor to the next line). It acts as a bridge between your code's inner"
                "\n\t workings and the outside world, allowing you to see the results of your calculations," 
                "\n\tinspect the values of variables, and provide feedback to the user."
                 )
                
            elif num_fun1 == 2:
                print( "\n\n\n\tBasic Usage:"
                       "\n\n\tInput: print('Hello, world!')  \t\tOutput: Hello, world!"

                        "\n\n\n\tBasic Usage:"
                        "\n\n\tInput:print('apple', 'banana', 'cherry', sep=',' , end=). \t\tOutput: apple, banana, cherry.")

            elif num_fun1 == 0:
                Clear()
                num_py_funda = input("\n\n\tPrinting In Python Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()

                if num_py_funda == "YES":
                    Clear()
                    print("\n\tThe Printing In Python Menu will mow be terminated.")
                    break

                elif num_py_funda == "NO":
                    Clear()
                    print("\n\tThe Printing In Python Menu will now continue.")
                    continue

            elif num_fun1 < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif num_fun1 >= 4:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Invalid Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue
                         
def Func():
    while True:
        try:
            print("\n\n\t-----------------------------------------------------------------------------------------"
                     "\n\t----------------------------<Function In Python Menu>----------------------------------"
                     "\n\t----------------------------------------------------------------------------------------"
                     "\n\t1.Definition \n\t2.Examples \n\t3.Return to Main Menu "
            )
            num_fun1 = int(input("Enter the number of your choice:"))

            if num_fun1 == 1:
                print( "\n\n\tThe print() function takes one or more arguments, which are converted"
                "\n\t into strings and then written to the console, followed by a newline character" 
                "\n\t(moving the cursor to the next line). It acts as a bridge between your code's inner"
                "\n\t workings and the outside world, allowing you to see the results of your calculations," 
                "\n\tinspect the values of variables, and provide feedback to the user."
                 )
                
            elif num_fun1 == 2:
                print( 
                    
                        "\n\n\n\tBasic Usage:"
                        "\n\n\tInput: print('Hello, world!')  \t\tOutput: Hello, world!"

                        "\n\n\n\tBasic Usage:"
                        "\n\n\tInput:print('apple', 'banana', 'cherry', sep=', ', end=). \t\tOutput: apple, banana, cherry."
                )

            elif num_fun1 == 0:
                Clear()
                num_py_funda = input("\n\n\tPrinting In Python Menu has stopped."
                                "\n\tDo you want to continue? (Yes or No) ").upper().strip()

                if num_fun1 == "YES":
                    Clear()
                    print("\n\tThe Printing In Python Menu will mow be terminated.")
                    break

                elif num_fun1 == "NO":
                    Clear()
                    print("\n\tThe Printing In Python Menu will now continue.")
                    continue

            elif num_fun1 < 0:
                print("\n\tError. Please enter a positive number.")
                continue
            elif num_fun1 >= 4:
                print("\n\tError. Please enter a number from the given choices.")
                continue
            else:
                Clear()
                print("\n\tError. Invalid Input")
                continue
        except ValueError:
            Clear()
            print("\n\tError. Please enter a real number.")
            continue
                         
def Var():
    pass
def Loops():
    pass
def Condi():
    pass
def List():
    pass
def Opera():
    pass

Main_Menu()