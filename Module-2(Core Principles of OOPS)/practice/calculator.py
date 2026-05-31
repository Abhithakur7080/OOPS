class ShapeCalculator:

    # Area of Circle / Rectangle / Trapezoid (simulated overloading)
    def area(self, *args):

        # Area of Circle
        if len(args) == 1:
            radius = args[0]
            ans = 3.14 * radius * radius
            print("Area of Circle :", int(ans))

        # Area of Rectangle
        elif len(args) == 2:
            length, width = args
            ans = length * width
            print("Area of Rectangle :", ans)

        # Area of Trapezoid
        elif len(args) == 3:
            base1, base2, height = args
            ans = 0.5 * (base1 + base2) * height
            print("Area of Trapezoid :", int(ans))


def main():
    # Hardcoded inputs
    radius = 2
    length = 2
    width = 3
    base1 = 2
    base2 = 3
    height = 2

    # Create object and call overloaded methods
    calc = ShapeCalculator()
    calc.area(radius)
    calc.area(length, width)
    calc.area(base1, base2, height)


if __name__ == "__main__":
    main()
