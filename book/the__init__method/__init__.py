class Rectangle:
    def area( self ):
        return self.width * self.height

rectangle = Rectangle()  # 这里需要加括号
rectangle.width, rectangle.height = 1, 2
print(rectangle.area())
