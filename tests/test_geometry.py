import pytest

import geometry


class TestIsRightAngleTriangle:
    def test_is_right_angle_triangle(self):
        assert geometry.is_right_angle_trianle(3, 4, 5)
