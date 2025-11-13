# Program to calculate due amount (change) using def, continue, and break

def calculate_change():
    while True:
        try:
            bill = float(input("Enter the total bill amount: $"))
            paid = float(input("Enter the amount paid: $"))

            if bill <= 0 or paid <= 0:
                print("Amounts must be positive. Try again.\n")
                continue  # ask again

            if paid < bill:
                print(f"You still owe ${bill - paid:.2f}\n")
                pass  # just continue to next iteration
            else:
                change = paid - bill
                print(f"The shopkeeper should return ${change:.2f}\n")
                break  # exit loop after successful calculation

        except ValueError:
            print("Invalid input! Please enter numbers only.\n")
            continue  # ask again if invalid input

# Call the function
calculate_change()
