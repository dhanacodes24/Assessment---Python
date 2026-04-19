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