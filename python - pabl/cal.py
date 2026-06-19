#!/usr/bin/env python3
"""Simple interactive calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Power", power),
    }

    print("Basic Calculator")
    print("----------------")

    while True:
        print("\nSelect an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please choose a valid option.")
            continue

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")
        name, func = operations[choice]

        try:
            result = func(a, b)
        except Exception as err:
            print(f"Error: {err}")
        else:
            print(f"{name} result: {result}")


if __name__ == "__main__":
    main()
