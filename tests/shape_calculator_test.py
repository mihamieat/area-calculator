# -*- coding: utf-8 -*-
"""Unit test module."""
import unittest
from src.area_calculator import shape_calculator


class UnitTests(unittest.TestCase):
    """
    Unit tests for the ShapeCalculator class.

    This class contains unit tests for various methods of the ShapeCalculator class.

    No Args or Returns.
    """

    maxDiff = None

    def setUp(self):
        """
        Sets up the initial state for the unit tests.

        No Args or Returns.
        """

        self.rect = shape_calculator.Rectangle(3, 6)
        self.sq = shape_calculator.Square(5)

    def test_subclass(self):
        """
        Tests if the Square class is a subclass of the Rectangle class.

        No Args or Returns.
        """

        actual = issubclass(shape_calculator.Square, shape_calculator.Rectangle)
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected Square class to be a subclass of the Rectangle class.",
        )

    def test_distinct_classes(self):
        """
        Tests if the Square class is a distinct class from the Rectangle class.

        No Args or Returns.
        """

        actual = shape_calculator.Square is not shape_calculator.Rectangle
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected Square class to be a distinct class from the Rectangle class.",
        )

    def test_square_is_square_and_rectangle(self):
        """
        Tests if the square object is an instance of both the Square class and the Rectangle class.

        No Args or Returns.
        """

        actual = isinstance(self.sq, shape_calculator.Square) and isinstance(
            self.sq, shape_calculator.Rectangle
        )
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected square object to be an instance of the Square class and the Rectangle class.",
        )

    def test_rectangle_string(self):
        """
        Tests the string representation of the rectangle object.

        No Args or Returns.
        """

        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of rectangle to be "Rectangle(width=3, height=6)"',
        )

    def test_square_string(self):
        """
        Tests the string representation of the square object.

        No Args or Returns.
        """

        actual = str(self.sq)
        expected = "Square(side=5)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square to be "Square(side=5)"',
        )

    def test_area(self):
        """
        Tests the calculation of the area for the rectangle and square objects.

        No Args or Returns.
        """

        actual = self.rect.get_area()
        expected = 18
        self.assertEqual(actual, expected, "Expected area of rectangle to be 18")
        actual = self.sq.get_area()
        expected = 25
        self.assertEqual(actual, expected, "Expected area of square to be 25")

    def test_perimeter(self):
        """
        Tests the calculation of the perimeter for the rectangle and square objects.

        No Args or Returns.
        """

        actual = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, "Expected perimeter of rectangle to be 18")
        actual = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected, "Expected perimeter of square to be 20")

    def test_diagonal(self):
        """
        Tests the calculation of the diagonal for the rectangle and square objects.

        No Args or Returns.
        """

        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        self.assertEqual(
            actual, expected, "Expected diagonal of rectangle to be 6.708203932499369"
        )
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        self.assertEqual(
            actual, expected, "Expected diagonal of square to be 7.0710678118654755"
        )

    def test_set_attributes(self):
        """
        Tests the setting of attributes and the string representation of the "\
        "rectangle and square objects.

        No Args or Returns.
        """

        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of rectangle after setting new values"\
            " to be "Rectangle(width=7, height=8)"',
        )
        actual = str(self.sq)
        expected = "Square(side=2)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square after setting new values"\
            "to be "Square(side=2)"',
        )
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square after setting width to be "Square(side=4)"',
        )

    def test_rectangle_picture(self):
        """
        Tests the generation of the picture representation for the rectangle object.

        No Args or Returns.
        """

        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        self.assertEqual(
            actual, expected, "Expected rectangle picture to be different."
        )

    def test_square_picture(self):
        """
        Tests the generation of the picture representation for the square object.

        No Args or Returns.
        """

        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        self.assertEqual(actual, expected, "Expected square picture to be different.")

    def test_big_picture(self):
        """
        Tests the generation of the picture representation for a rectangle object "\
        "that is too big for a picture.

        No Args or Returns.
        """

        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture."
        self.assertEqual(actual, expected, 'Expected message: "Too big for picture."')

    def test_get_amount_inside(self):
        """
        Tests the calculation of the number of times the given shape can fit inside"\
        " the current shape.

        No Args or Returns.
        """

        self.rect.set_height(10)
        self.rect.set_width(15)
        actual = self.rect.get_amount_inside(self.sq)
        expected = 6
        self.assertEqual(actual, expected, "Expected `get_amount_inside` to return 6.")

    def test_get_amount_inside_two_rectangles(self):
        """
        Tests the calculation of the number of times the given shape can fit "\
        "inside the current shape.

        No Args or Returns.
        """

        rect2 = shape_calculator.Rectangle(4, 8)
        actual = rect2.get_amount_inside(self.rect)
        expected = 1
        self.assertEqual(actual, expected, "Expected `get_amount_inside` to return 1.")

    def test_get_amount_inside_none(self):
        """
        Tests the calculation of the number of times the given shape can fit "\
        "inside the current shape.

        No Args or Returns.
        """

        rect2 = shape_calculator.Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        self.assertEqual(actual, expected, "Expected `get_amount_inside` to return 0.")


if __name__ == "__main__":
    unittest.main()
