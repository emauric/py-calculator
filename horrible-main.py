# Complete Functions #
class Calculator:
    def add(self):
        """Adds together two input numbers"""
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            print(f"The sum is: {total}\n")
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

    def subtract(self):
        """Subtracts one input from another input number"""
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            print(f"The difference is: {total}\n")
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

    def multiply(self):
        """Multiplies two input numbers"""
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            print(f"The product is: {total}\n")
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

    def divide(self):
        """Divides one input with another input number"""
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num2 == 0:
                print("Division by zero is not allowed.")
                return

            total = num1 // num2
            remainder = num1 % num2
            print(f"The quotient is: {total} with a remainder of {remainder}\n")
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")


def menu():
    """ Menu for choosing between each function """
    calculator = Calculator()

    while True:

        print("===Calculator Menu===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            calculator.add()
        elif choice == "2":
            calculator.subtract()
        elif choice == "3":
            calculator.multiply()
        elif choice == "4":
            calculator.divide()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please select a valid option.\n")

# Run the Menu


menu()
