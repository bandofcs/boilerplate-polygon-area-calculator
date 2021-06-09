class Rectangle:
    def __init__(self,width,height):
        self.set_width(width)
        self.set_height(height)

    def __str__ (self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        output=""
        if self.height>50 or self.width>50:
            return "Too big for picture."
        else:         
            for row in range(self.height):
                for column in range(self.width):
                    output=output+"*"
                output=output+"\n"
        return output

    def get_amount_inside(self,Rectangle):
        if self.height<Rectangle.height or self.width<Rectangle.width:
            return 0
        else:
            return (self.height//Rectangle.height)*(self.width//Rectangle.width)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def __str__(self):
        return "Square(side="+str(self.width)+")"

    def set_side(self,width):
        self.set_width(width)
        self.set_height(width)
