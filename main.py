from simple_calculator import SimpleCalculator
from geometry_tool import GeometryTool

def main():
    calc = SimpleCalculator()
    geo = GeometryTool()

    while True:
        print("""
        === SHAPEMATH CALCULATOR ===
        1. Simple Calculator
        2. Geometry Tool
        3. Exit
        ============================
        """)

        main_choice = input("Enter an option (1/2/3): ").strip().lower()
        match main_choice:
            case "1" | "one":
                run_calculator(calc)
            case "2" | "two":
                run_geometry_tool(geo)
            case "3" | "three":
                print("Thank you for using ShapeMath.")
                break
            case _:
                print("Please enter a valid option")

def run_calculator(calc: SimpleCalculator):
    while True:
        print("""
        === SIMPLE CALCULATOR MENU ===
        1. Calculate
        2. Show History
        3. Clear History
        4. Return to Main Menu
        ==============================
        """)

        choice = input("Enter an option (1/2/3/4): ").strip().lower()
        match choice:
            case "1" | "one":
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
                op = input("Enter operator (+, -, *, **, /, //, %): ")
                result = calc.calculate(n1, n2, op)

                print(f"\n >>> Result: {result}")
            case "2" | "two": calc.show_history()
            case "3" | "three": calc.clear_history()
            case "4" | "four": return
            case _: print("Please enter a valid option.")

def run_geometry_tool(geo: GeometryTool):
    while True:
        print("""
        === GEOMETRY TOOL MENU ===
        1. Calculate Area (2D shape)
        2. Calculate Volume (3D shape)
        3. Return to Main Menu
        ==========================
        """)

        choice = input("Enter an option (1/2/3): ").strip().lower()
        match choice:
            case "1" | "one": geo.run_tool("2D")
            case "2" | "two": geo.run_tool("3D")
            case "3" | "three": return
            case _: print("Please enter a valid option.")

if __name__ == "__main__":
    main()