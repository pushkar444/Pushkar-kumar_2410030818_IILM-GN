#!/usr/bin/env python3
"""
Simple Interactive Calculator in Python.
Provides basic operations like Addition, Subtraction, Multiplication, Division, and Exponentiation.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of division, raising ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Returns the result of base a raised to power b."""
    return a ** b


def get_numeric_input(prompt):
    """Helper function to ensure user inputs a valid numeric value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 5 or 3.14).")


def main():
    # Define operations with description and function mapping
    operations = {
        "1": ("Add (+)", add),
        "2": ("Subtract (-)", subtract),
        "3": ("Multiply (*)", multiply),
        "4": ("Divide (/)", divide),
        "5": ("Power (^)", power),
    }

    print("================================")
    print("      Python Calculator         ")
    print("================================")

    while True:
        print("\nSelect an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Enter selection (1-5 or q): ").strip().lower()

        if choice == 'q':
            print("Thank you for using the Python Calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a valid number between 1 and 5, or 'q' to quit.")
            continue

        name, operation_func = operations[choice]
        print(f"\n--- {name} Operation ---")
        
        num1 = get_numeric_input("Enter the first number: ")
        num2 = get_numeric_input("Enter the second number: ")

        try:
            result = operation_func(num1, num2)
            # Format output nicely: show integers as integers, floats as floats
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            print(f"\nResult: {formatted_result}")
        except ValueError as err:
            print(f"\nError: {err}")
        except Exception as err:
            print(f"\nAn unexpected error occurred: {err}")


if __name__ == "__main__":
    main()
