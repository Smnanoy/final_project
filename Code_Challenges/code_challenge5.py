def code_challenge5():

    print("==============================================")

    fahrenheit = eval(input("Enter your temperature in farenheit ---> "))

    celsius  = ((fahrenheit - 32) * 5 ) / 9

    print( fahrenheit, "degrees fahrenheit converted to celsius is" ,celsius, "degrees" )

    print(f" {fahrenheit}degrees, fahrenheit converted to celsius is {celsius}degrees" )
    print(round(celsius, 2 ))

    print("==============================================")

    print(f" {fahrenheit}degrees fahrenheit converted to celsius is {round(celsius, 2)}degrees" )