# Customer Banking

Script for customer banking system that prompts the user to enter the savings and cd account balance, interest rate, and the length of months to determine the interest gained.

## Description

__Customer Banking script (customer_banking.py)__ (main script) imports two functions that, when passed three arguments, calcuate interest earned from two different account types.

* __Account module (Account.py)__ defines a class object (Account) which sets the account balance and sets the interest earned for a custmer account

* __CD Account module (cd_account.py)__ and __Savings Account module (savings_account.py)__ each accept the balance, interest rate and time to maturity as arguments and calcuate the the amount of interest earned and the balance when the accounts reach maturity. Each of these modules also create and instance of the Account class (for a savings account and a cd account), and pass the interst amount earned and updated balance to their respective account class instances.

### Skills Demonstrated

The primary skills demonstrated include the ability to:
* Create reusable, modular code 
* Create and use multiple instances of a class object 

### Dependencies

Python Modules
* Account.py (Account class object)
* cd_account.py (function for calcuating interest earned on a cd account)
* savings_account.py (function for calcuating interest earned on a savings account)
* customer_banking (main script to capture user, import functions and display outputs)

Python Libraries
* No special libraries required

## Authors

Jamie Bond | jamie.l.bond@outlook.com | [Connect on Linkedin](https://linkedin.com/in/jamielbond)

## Acknowledgments

Adapted from starter files provided by [The Artificial Intelligence Boot Camp at UNC Charlotte](https://bootcamp.charlotte.edu/artificial-intelligence/), including:
* Accounts.py 
* cd_acount.py
* savings_acount.py
* customer_banking.py


