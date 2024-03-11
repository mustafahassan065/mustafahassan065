def show_expenses():
    portions = []
    expenses = []

    num_portions = int ( input("Enter the number of catgories "))
    for i in num_portions:
        portion = input(f"Enter the category name {i+1}")
        amount = float(input(f"Enter the amount for {portion}"))
        portions.append(portion)
        expenses.append(amount)

        return portion , expenses
    
def show_income():
    income = float(input("Enter you income"))
    return income
def show_data(portions , expenses, income):
    print("The list of Expenses with Categories")
    for portion , amount in zip(portions,expenses):
        print(f'{portion}:{amount:.2f}')

        total_expenses = sum(expenses)
        print(f'Total Expenses: ${total_expenses:.2f}')
        print(f'income : ${income:.2f}')
        print(f'Remaining balance:${income - total_expenses:.2f }')


def main():
    portions , expenses = show_expenses
    income = show_income()
    show_data(portions,expenses,income)

main()



