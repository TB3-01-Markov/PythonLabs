
class Rectangle:

    def __init__(self, a=1, b=1):
        #print("TEST __init__(self, l, w)")
        self.side_a = Rectangle.check_value(a)
        self.side_b = Rectangle.check_value(b)

    def rectanglePerimeter(self):
        #print("TEST rectanglePerimeter(self)")
        return 2 * (self.side_a + self.side_b)

    def rectangleArea(self):
        #print("TEST rectangleArea(self)")
        return (self.side_a * self.side_b)

    def check_value(value):
        #print("TEST check_value")
        if(value<=0.0):
            print("given side of rectangle ", value," <=0 is less than allowed value")
            raise Exception
        elif (value>=20.0):
            print("given side of rectangle ", value," >= 20 exceeds allowed value")
            raise Exception
        else:
            return value

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'HELLO THERE, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('HERE IS MARKOV FROM TB301')
    newRectangle = Rectangle(5, 10)
    print("side A of rectangle: ", newRectangle.side_a)
    print("side B of rectangle: ", newRectangle.side_b)
    print("rectangle Area ", newRectangle.rectangleArea())
    print("rectangle Perimeter ", newRectangle.rectanglePerimeter())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
