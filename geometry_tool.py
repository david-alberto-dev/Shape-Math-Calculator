import math

class GeometryTool:
    def __init__(self):
        self.shape_inputs = {
            "triangle": ["base", "height"],
            "circle": ["radius"],
            "square": ["side"],
            "rectangle": ["length", "width"],
            "rhombus": ["diag1", "diag2"],
            "parallelogram": ["base", "height"],
            "pyramid": ["base_side", "height"],
            "cone": ["radius", "height"],
            "sphere": ["radius"],
            "cube": ["side"],
            "cylinder": ["radius", "height"],
            "rectangular_prism": ["side", "width", "height"]
        }

        self.shapes_2d = {
            "triangle": self.area_triangle,
            "circle": self.area_circle,
            "square": self.area_square,
            "rectangle": self.area_rectangle,
            "rhombus": self.area_rhombus,
            "parallelogram": self.area_parallelogram
        }

        self.shapes_3d = {
            "pyramid": self.volume_pyramid,
            "cone": self.volume_cone,
            "sphere": self.volume_sphere,
            "cube": self.volume_cube,
            "cylinder": self.volume_cylinder,
            "rectangular_prism": self.volume_rectangular_prism
        }

    def area_triangle(self, base, height):
        return base * height * 0.5

    def area_circle(self, radius):
        return math.pi * radius ** 2

    def area_square(self, side):
        return side ** 2

    def area_rectangle(self, length, width):
        return length * width

    def area_rhombus(self, diag1, diag2):
        return diag1 * diag2 * 0.5

    def area_parallelogram(self, base, height):
        return base * height

    def volume_pyramid(self, base_side, height):
        return (base_side ** 2) * height * (1 / 3)

    def volume_cone(self, radius, height):
        return (1 / 3) * math.pi * radius ** 2 * height

    def volume_cube(self, side):
        return side ** 3

    def volume_sphere(self, radius):
        return (4 / 3) * math.pi * radius ** 3

    def volume_cylinder(self, radius, height):
        return math.pi * radius ** 2 * height

    def volume_rectangular_prism(self, side, width, height):
        return side * width * height

    def get_number(self, prompt):
        while True:
            try:
                val = float(input(prompt))
                if val <= 0:
                    print("Value must be greater than 0")
                    continue
                return val
            except ValueError:
                print("Please enter a number")

    def run_tool(self, category):
        if category == "2D":
            print(f"\nAvailable shapes: {', '.join(self.shapes_2d.keys())}")
            choice = input("Enter shape name: ").strip().lower()

            if choice in self.shapes_2d.keys():
                requirements = self.shape_inputs[choice]
                values = []
                for item in requirements:
                    num = self.get_number(f"Enter {item}: ")
                    values.append(num)
                result = self.shapes_2d[choice](*values)
                print(f"\n >>> Result: {result:.2f} square units.")

            else:
                print("Shape not found.")

        elif category == "3D":
            print(f"\nAvailable shapes: {', '.join(self.shapes_3d.keys())}")
            choice = input("Enter shape name: ").strip().lower()

            if choice in self.shapes_3d.keys():
                requirements = self.shape_inputs[choice]
                values = []
                for item in requirements:
                    num = self.get_number(f"Enter {item}: ")
                    values.append(num)
                result = self.shapes_3d[choice](*values)
                print(f"\n >>> Result: {result:.2f} cubic units.")

            else:
                print("Shape not found.")