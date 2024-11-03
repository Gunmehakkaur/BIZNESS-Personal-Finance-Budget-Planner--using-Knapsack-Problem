# Function to take user inputs for income and expenses
def get_user_input():
    # Get total monthly income from the user
    income = float(input("Enter your total monthly income in Rupees: "))
    
    # Initialize an empty list for expenses
    expenses = []
    
    # Loop to add expenses
    while True:
        name = input("Enter expense name (or type 'done' to finish): ")
        if name.lower() == 'done': #case sensitive
            break
        
        try:#error handling
            cost = float(input(f"Enter cost for {name} in Rupees: "))
            priority = int(input(f"Enter priority for {name} (1-5, where 5 is the highest priority): "))
            if priority < 1 or priority > 5:
                print("Priority must be between 1 and 5.")
                continue
        except ValueError:#exception handling 
            print("Invalid input. Please enter numbers for cost and priority.")
            continue

        # Add the expense as a dictionary to the expenses list
        expenses.append({"name": name, "cost": cost, "priority": priority})
    
    return income, expenses

# Knapsack algorithm to find optimal allocation based on priorities
def knapsack_budget_allocation(income, expenses):
    # Sort expenses by priority and then by cost for items with the same priority
    expenses = sorted(expenses, key=lambda x: (-x['priority'], x['cost']))
    
    total_cost = 0
    recommended_expenses = []
    not_recommended_expenses = []
    
    # Select expenses based on priority and ensure they fit within the budget
    for expense in expenses:
        if total_cost + expense["cost"] <= income:
            recommended_expenses.append(expense)
            total_cost += expense["cost"]
        else:
            not_recommended_expenses.append(expense)
    
    return recommended_expenses, not_recommended_expenses, total_cost

# Main program
income, expenses = get_user_input()
recommended_expenses, not_recommended_expenses, total_cost = knapsack_budget_allocation(income, expenses)

# Output the budget recommendation
print("\nRecommended Budget Allocation:")
for expense in recommended_expenses:
    print(f"- {expense['name']}: Rupees{expense['cost']} (Priority: {expense['priority']})")

# Show items that were not included in the budget
print("\nExpenses Not Recommended or Exceeding Budget):")
for expense in not_recommended_expenses:
    print(f"- {expense['name']}: Rupees{expense['cost']} (Priority: {expense['priority']})")

# Calculate remaining income (savings)
remaining_income = income - total_cost
print(f"\nTotal Allocated: Rupees{total_cost}")
print(f"Remaining Income (Savings): Rupees{remaining_income}")
