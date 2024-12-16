
def code_challenge16():

    def breakdown_denom(amount):    
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        breakdown = {}

        for denom in denominations:
            count = amount // denom
            if count > 0:
                breakdown[denom] = count
            amount = amount % denom
        
        return breakdown 

    def create_account():
        name = input("Enter your name: ")
        balance = float(input("Enter initial deposit: "))
        print(f"Account made for {name} with an initial balance of {balance}.")
        return name, balance

    def show_balance(balance):
        print(f"Current balance: {balance}")
        
    def deposit(balance):
        deposit_amount = float(input("Enter deposit amount: "))
        balance += deposit_amount
        print(f"Deposited: {deposit_amount}")
        return balance

    def withdraw(balance):
        withdraw_amount = float(input("Enter withdrawal amount: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawn: {withdraw_amount}")
        else:
            print("Not enough funds.")
        return balance

    def main():
        name, balance = create_account()

        while True:
            print("\nBanking options: \n1. Deposit \n2. Withdraw \n3. View Balance")
            print("4. Breakdown of Denominations \n5. Terminate")

            chosen_operator = input("Choose an operation: ")
            
            if chosen_operator == '1':
                balance = deposit(balance)
                
            elif chosen_operator == '2':
                balance = withdraw(balance)
                    
            elif chosen_operator == '3':
                show_balance(balance)
                
            elif chosen_operator == '4':
                print("\nDenomination Breakdown:")
                show_balance(balance)
                    
            elif chosen_operator == '5':
                print("Thank you for using the program.")
                break
            
            else:
                print("Invalid input. Please select only the given operations.")

    if __name__ == "__main__":
        main()
    