import pytest

from src.Figure import Figure
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle

@pytest.mark.parametrize("a, b, c, res", [(13, 14, 15, 84.0)])
def test_area_triangle(a,b, c, res):
    triangle = Triangle(a, b, c)
    triangle.area_triangle()
    assert triangle.area == res

@pytest.mark.parametrize("a, b, res", [(5, 4, 20)])
def test_area_rectangle(a, b, res):
    rectangle = Rectangle(a, b)
    rectangle.area_rectangle()
    assert rectangle.area == res

@pytest.mark.parametrize("a, res", [(10, 100)])
def test_area_square(a, res):
    squara = Square(a)
    squara.area_squara()
    assert squara.area == res

@pytest.mark.parametrize("r, res", [(5, 78.5398)])
def test_area_circle(r, res):
    circle = Circle(r)
    circle.area_circle()
    assert circle.area == res

@pytest.mark.parametrize("a, b, c", [(13, 14, 44)])
def test_triangle_value_error(a,b, c):
    with pytest.raises(ValueError):
        triangle = Triangle(a,b, c)

@pytest.mark.parametrize("a_tr, b_tr, c_tr, ", [(13, 14, 15)])
@pytest.mark.parametrize("a_rec, b_rec, ", [(5, 4)])
@pytest.mark.parametrize("res", [104.0])
def test_add_area(a_tr, b_tr, c_tr, a_rec, b_rec, res):
    triangle = Triangle(a_tr, b_tr, c_tr)
    triangle.area_triangle()
    rectangle = Rectangle(a_rec, b_rec)
    rectangle.area_rectangle()
    result = triangle.add_area(rectangle)
    assert result == res
