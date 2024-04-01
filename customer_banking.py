# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
1000

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance_input = input("\nEnter current savings account balance: $")
    savings_interest_input = input("Enter the annual interest rate on the savings account (percentage points): ")
    savings_maturity_input = input("How long will the balance remain in the savings account (No. of months): ")

    savings_balance = float(savings_balance_input)
    savings_interest = float(savings_interest_input)
    savings_maturity = int(savings_maturity_input)
   
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nAfter {savings_maturity} months, this savings account will earn ${interest_earned:.2f}.")
    print(f"Your updated saving balance will be ${updated_savings_balance:.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance_input = input("\nEnter current cd account balance: $")
    cd_interest_input = input("Enter the annual interest rate on the cd account: (percentage points) ")
    cd_maturity_input= input("How long will the balance remain in the cd account (No. of months): ")

    cd_balance = float(cd_balance_input)
    cd_interest = float(cd_interest_input)
    cd_maturity = int(cd_maturity_input) 
    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nAfter {cd_maturity} months, this savings account will earn ${interest_earned:.2f}.")
    print(f"Your updated cd balance will be ${updated_cd_balance:.2f}.")

if __name__ == "__main__":
    # Call the main function.
    main()