# -*- coding: utf-8 -*-
"""Shape calculator modules."""


class Rectangle:
    """
    When a Rectangle object is created, it should be initialized with width and height attributes.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes a ShapeCalculator object with the given width and height.

        Args:
            width (float): The width of the shape.
            height (float): The height of the shape.

        Returns:
            None
        """
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float):
        """
        Sets the width of the shape.

        Args:
            width (float): The width to set.

        Returns:
            None
        """
        self.width = width
        return self.width

    def set_height(self, height: float):
        """
        Sets the height of the shape and returns the updated height.

        Args:
            height (float): The height to set.

        Returns:
            float: The updated height.
        """
        self.height = height
        return self.height

    def get_area(self):
        """
        Calculates and returns the area of the shape.

        Returns:
            float: The area of the shape.
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Calculates and returns the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Calculates and returns the diagonal length of the shape.

        Returns:
            float: The diagonal length of the shape.
        """

        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        """
        Generates a string representation of the shape as a picture.

        Returns:
            str: The picture of the shape if width not more than 50.
        """
        if self.width > 50:
            return "Too big for picture."
        return "".join(f"{'*' * self.width}\n" for _ in range(self.height))

    def get_amount_inside(self, shape_obj):
        """
        Calculates and returns the number of times the given shape can fit inside the current shape.

        Args:
            shape_obj (ShapeCalculator): The shape object to compare.

        Returns:
            float: The number of times the given shape can fit inside the current shape.
        """
        return self.get_area() // shape_obj.get_area()


class Square(Rectangle):
    """Subclass of Rectangle."""

    def __init__(self, side):
        """
        Initializes a Square object with the given side length.

        Args:
            side (float): The length of the side of the square.

        Returns:
            None
        """
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        """
        Sets the side length of the square.

        Args:
            side (float): The length of the side to set.

        Returns:
            None
        """
        super().set_height(side)
        super().set_width(side)
