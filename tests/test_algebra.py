import pytest

import algebra


class TestGetXInterceptsOfLine:
    def test_get_x_intercepts_of_line_zero(self):
        assert algebra.get_x_intercept_of_line(5, 0) == 0

    def test_get_x_intercepts_of_line_non_zero(self):
        assert algebra.get_x_intercept_of_line(5, 1) == (-1 / 5)
        assert algebra.get_x_intercept_of_line(10, 3) == (-3 / 10)


class TestQuadratic:
    def test_has_x_intercepts_1(self):
        # -2x^2 + x + 3
        assert [-1.0, 1.5] == algebra.quadratic(-2, 1, 3)

    def test_has_x_intercepts_2(self):
        # x^2 - 4
        assert [-2.0, 2.0] == algebra.quadratic(1, 0, -4)

    def test_has_x_intercepts_3(self):
        # 3x^2 + 3x
        assert [-1.0, 0] == algebra.quadratic(3, 3, 0)

    def test_has_one_x_intercept_1(self):
        # x^2
        assert [0] == algebra.quadratic(1, 0, 0)

    def test_has_one_x_intercept_2(self):
        # -x^2
        assert [0] == algebra.quadratic(-1, 0, 0)

    def test_has_no_x_intercepts_1(self):
        # x^2 + 1 : no X intercepts
        assert [] == algebra.quadratic(1, 0, 1)

    def test_has_no_x_intercepts_2(self):
        # -x^2 - 1 : no X intercepts
        assert [] == algebra.quadratic(-1, 0, -1)

    def test_is_not_a_quadratic_function(self):
        # 0x^2 + 1x + 0 : isn't a quadratic
        with pytest.raises(ValueError):
            algebra.quadratic(0, 1, 0)


class TestIntersection:
    def test_for_intersection(self):
        assert algebra.intersection(2, 1, 3, 1) == (0, 1)
        assert algebra.intersection(-3, 3, (1 / 5), 3) == (0, 3)

    def test_for_no_intersection(self):
        with pytest.raises(ValueError):
            algebra.intersection(0, 1, 0, 2)
