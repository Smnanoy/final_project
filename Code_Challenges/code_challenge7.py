def code_challenge7():

    print("Hello, Welcome to our Shop! ")
    name = input("Please enter your name: ")
    age = eval(input("Enter your age: "))
    isBuy = input(" Do you want to buy an item? ")

    if isBuy.lower() == "yes":
        Item_name = input("Name of the Item: ")
        Item_price = eval(input("Price of the Item: "))
        amountGiven = eval(input("Given amount: "))
        
        discount = round((Item_price*0.052),2)
        discount_Price = round((Item_price - discount),2)
        tax = round((Item_price * 0.123),2)
        tax_price = round((Item_price - tax),2)
        
    if age >=60:
        print(f"Hi {name}, you purchased a {Item_name}, with a price of {Item_price}php plus a 5.2% discount ({discount}php) to your total purchased")
        print(f"Total of: {round((Item_price - discount),2)} ")
        print(f"Change: {round((amountGiven - discount_Price),2)} ")
        print(f"Thank you for shopping with us, please come again.")
        
    elif age >=18:
        print(f"Hi {name}, you purchased a {Item_name}, with a price of {Item_price}php plus a 12.3% tax ({tax}php) to your total purchased")
        print(f"Total of: {round((Item_price + discount),2)} ")
        print(f"Change: {round((amountGiven - discount_Price),2)} ")
        print(f"Thank you for shopping with us, please come again.")
        

        
    else:     
        print("Thank you for shopping with us, have a good day ")