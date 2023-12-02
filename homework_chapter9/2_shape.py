# 定义一个shape类，利用它作为基类派生出Rectangle、Circle等据图形状，
# 已知具体形状类均具有两个方法GetArea和GetColor，分别用来得到形状的面积和颜色。
import math


class Shape:
    def __init__(self, color):
        self.color = color

    def GetArea(self):
        pass

    def GetColor(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


# 测试
if __name__ == "__main__":
    # 创建一个矩形对象
    rectangle = Rectangle(color="Blue", width=4, height=5)

    # 输出矩形的面积和颜色
    print("矩形面积:", rectangle.get_area())
    print("矩形颜色:", rectangle.GetColor())

    # 创建一个圆形对象
    circle = Circle(color="Red", radius=3)

    # 输出圆形的面积和颜色
    print("圆形面积:", circle.get_area())
    print("圆形颜色:", circle.GetColor())
