# Simple Calculator Program in Python
# Supports 4 basic operations: Addition, Subtraction, Multiplication, and Division

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, handling division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("=" * 30)
    print("       SIMPLE CALCULATOR       ")
    print("=" * 30)
    print("Select an operation:")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (*)")
    print("  4. Divide (/)")
    print("  q. Quit")
    print("=" * 30)

    while True:
        choice = input("\nEnter choice (1/2/3/4 or +,-,*,/) [q to quit]: ").strip()

        if choice.lower() == 'q':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numeric values.")
                continue

            if choice in ('1', '+'):
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice in ('2', '-'):
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice in ('3', '*'):
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice in ('4', '/'):
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or q.")

if __name__ == "__main__":
    main()
