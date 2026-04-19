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