

--------------------

## $\Large{\textcolor{#87CEEB}{\textbf{1. ATM widrawal System  }}}$ 

------------------

<details>
<summary>📄 <b>Click to expand — ATM widrawal System Code </b></summary>

```json

# ATM Withdrawal System

def atm_withdrawal(withdrawal_amount):
    current_balance = 5000  # fixed balance

    # Validation 1: Withdrawal amount must be greater than 0
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False

    # Validation 2: Withdrawal amount must be a multiple of 500
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False

    # Validation 3: Account balance must be sufficient
    if withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False

    # If all validations pass
    remaining_balance = current_balance - withdrawal_amount
    print(f"Withdrawal successful. Amount: {withdrawal_amount}")
    print(f"Remaining balance: {remaining_balance}")
    return True


# Accept input from user
try:
    amount = int(input("Enter withdrawal amount: "))
    atm_withdrawal(amount)
except ValueError:
    print("Error: Please enter a valid integer amount")

```
</details>

---------------
Case 1 - Withdrawal amount must be greater than 0
-----------------

<img width="731" height="55" alt="image" src="https://github.com/user-attachments/assets/f95f9e60-add2-4a70-9395-ba2a9935a417" />


------------------
---------------
Case 2 - Withdrawal amount must be a multiple of 500
-----------------

<img width="734" height="51" alt="image" src="https://github.com/user-attachments/assets/f403eca2-acdf-4394-bd5a-0254fb6dc472" />

------------------
---------------
Case 3 -  Account balance must be sufficient
-----------------

<img width="706" height="47" alt="image" src="https://github.com/user-attachments/assets/dcceeb6e-13f1-45cd-bafd-5e0fa2756461" />

------------------
---------------
Final output - 
-----------------
<img width="717" height="66" alt="image" src="https://github.com/user-attachments/assets/b2f8528c-2727-4d87-aa52-6eb9e882fbd1" />

------------------


## $\Large{\textcolor{#87CEEB}{\textbf{ Login Authentication System }}}$

---------

<details>
<summary>📄 <b>Click to expand — Login Authentication System Code </b></summary>

```json

# Improved Login Authentication System

def validate_login(username, password):
    # Validation 1: Username length must be at least 5 characters
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
        return False

    # Validation 2: Password length must be at least 8 characters
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False

    # Validation 3: Password must contain at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print("Error: Password must contain at least one digit")
        return False

    # If all validations pass
    print("Login successful")
    return True


# Accept input from user
username = input("Enter username: ")

# Check username first before asking for password
if len(username) < 5:
    print("Error: Username must be at least 5 characters")
    print("Return: False")
else:
    password = input("Enter password: ")
    result = validate_login(username, password)
    print("Return:", result)

```
</details>

---------
---------------
Case 1 - Username length must be at least 5 characters
-----------------
------------------
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/ff723cda-200a-4fe2-8262-6c366debc7d9" />

------------------
---------------
Case 2 - Password length must be at least 8 characters
-----------------

<img width="500" height="84" alt="image" src="https://github.com/user-attachments/assets/f39f94e6-87ed-4418-b2e4-7e2592bd1c2f" />

------------------
---------------
Case 3 - Password must contain at least one digit
-----------------
<img width="506" height="89" alt="image" src="https://github.com/user-attachments/assets/8ae05b00-329d-4364-9c61-05efb071d5d5" />

------------------
---------------
Final output 
-----------------
<img width="435" height="83" alt="image" src="https://github.com/user-attachments/assets/d55f9265-1c2a-4848-a9df-c9d04461ee68" />

------------------


# $\Large{\textcolor{#87CEEB}{\textbf{ Restaurant bill calculator }}}$


------------------

<details>
<summary>📄 <b>Click to expand — Restaurant bill calculator  Code </b></summary>

```json

# Restaurant Bill Calculator

def calculate_restaurant_bill(meal_cost):
    # Service charge: 10% of meal cost
    service_charge = meal_cost * 0.10
    
    # Amount after service
    amount_after_service = meal_cost + service_charge
    
    # Tax: 5% of amount after service
    tax = amount_after_service * 0.05
    
    # Tip: 5% of amount after service
    tip_amount = amount_after_service * 0.05
    
    # Total bill
    total = amount_after_service + tax + tip_amount
    
    # Output format
    print(f"Meal Cost: {meal_cost}")
    print(f"Service Charge (10%): {service_charge}")
    print(f"Amount after Service: {amount_after_service}")
    print(f"Tax (5%): {tax}")
    print(f"Tip (5%): {tip_amount}")
    print(f"Total Bill: {total}")
    
    return total


# Accept input from user
try:
    meal_cost = float(input("Enter meal cost: "))
    calculate_restaurant_bill(meal_cost)
except ValueError:
    print("Error: Please enter a valid number")

```
</details>

---------------
Output - 
-----------------
-----------------

<img width="463" height="134" alt="image" src="https://github.com/user-attachments/assets/d7b92c4a-88d8-42b7-9de0-13dc0b997311" />

---------------



