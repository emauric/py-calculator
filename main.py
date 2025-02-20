# Complete Functions #
class Calculator:

    def get_numbers(self):
        """Gets two integer inputs from the user."""
        while True:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                return num1, num2
            except ValueError:
                print("Invalid input. Please enter numbers only.\n")

    def add(self, num1, num2):
        """Adds together two input numbers"""
        return num1 + num2

    def subtract(self, num1, num2):
        """Subtracts one input from another input number"""
        return num1 - num2

    def multiply(self, num1, num2):
        """Multiplies two input numbers"""
        return num1 * num2
    def divide(self, num1, num2):
        """Divides one input with another input number"""
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return f"{num1 // num2} with a remainder of {num1 % num2}"


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

        if choice in ["1","2","3","4"]:
            num1, num2 = calculator.get_numbers()

            operations = {
                "1": calculator.add,
                "2": calculator.subtract,
                "3": calculator.multiply,
                "4": calculator.divide
            }

            result = operations[choice](num1, num2)
            print(f"Result: {result}\n")

        elif choice == "5":
            break
        else:
            print("Invalid choice, please select a valid option.\n")

# Run the Menu


menu()
