def main():
    # Initialize an empty list to store daily sales
    sales = []

    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Prompt the user to enter sales for each day
    for day in days:
        sales_amount = float(input(f"Enter sales for {day}: $"))
        sales.append(sales_amount)

    # Calculate total sales for the week
    total_sales = sum(sales)

    # Display the total sales for the week
    print(f"\nTotal sales for the week: ${total_sales:.2f}")

if __name__ == "__main__":
    main()
