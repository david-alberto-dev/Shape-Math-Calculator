class SimpleCalculator:
    def __init__(self):
        self.history = []

    def calculate(self, num1, num2, op):
        try:
            match op:
                case "+": result = num1 + num2
                case "-": result = num1 - num2
                case "*": result = num1 * num2
                case "/": result = num1 / num2
                case "//": result = num1 // num2
                case "%": result = num1 % num2
                case _: return "Invalid operator!"
            self.history.append(f"{num1} {op} {num2} = {result}")
            return result

        except ZeroDivisionError:
            return "Division by zero is not possible."

        except ValueError:
            return "Please enter a number!"

        except Exception as err:
            return f"Error: {err}"

    def show_history(self):
        if not self.history:
            print("History is empty.")
        else:
            print("--- Calculator History ---")
            for i, c in enumerate(self.history, start=1):
                print(f"{i}. {c}")

    def clear_history(self):
        if not self.history:
            print("Nothing to clear, history was already empty.")
        else:
            self.history.clear()
            print("History cleared!")