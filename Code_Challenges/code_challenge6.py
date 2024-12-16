
def code_challenge6():

   print(" Good day, my fellow students!! ") 
   name = input(" Please enter your name: ")
   print("-----------------------------------------")

   prelim = eval(input(" Please enter your grades for the prelims --> "))
   midterm = eval(input(" Please enter your grades for the midterms --> "))
   s_finals = eval(input("Please enter your grades for the semifinals --> "))
   final = eval(input(" Please enter your grades for the finals --> "))
   quiz = eval(input(" Please enter your grades of your quizzes --> "))
   project = eval(input(" Please enter your grades of your projects --> "))
   print("------------------------------------------")


   if (prelim >= 74 and prelim <=100) and (midterm >= 74 and midterm <=100) and (s_finals >= 74 and s_finals <=100) and (final >= 74 and final <=100) and (quiz >= 74 and quiz <=100) and (project >= 74 and project <=100):
      Final_Grade = prelim*0.15 + midterm*0.15 + s_finals*0.15 + final*0.15 + quiz*0.15+ project*0.15
      (round(Final_Grade, 2))
      print(f" CONGRATULATIONS, {name}! Your final grade is {round(Final_Grade,2)} ")

   else:
      print(" Invalid Grades")
      
      
   if Final_Grade == 100:
      print(" --You passed-- ")
      print(" --WOW!, You're an amazing student!--")
      
   elif Final_Grade >= 95:
      print(" --You passed-- ")
      print(" --You did great!, So proud of you--")
      
   elif Final_Grade >= 90:
      print(" --You passed-- ")
      print(" --You did your best!, now smileee--")   
      
   elif Final_Grade >= 88:
      print(" --You passed-- ")
      print(" --Look who got an award, It's you! Yayyyy--")
      
   elif Final_Grade >= 80:
      print(" --You passed-- ")
      print(" --What an amazing ride is'nt it, Look you passed the course--")
      
   elif Final_Grade >= 75:
      print(" --You passed-- ")
      print(" --Almost there! But hey, you passed.-- ")   
      
   elif Final_Grade == 74:
      print(" --You failed-- ")
      print(" --What happened bro, unfortunately you fail--")   
      
   else:
      print(" --You failed-- ")
      print(" --See you next year--")

   print("----------------------------------------------------")