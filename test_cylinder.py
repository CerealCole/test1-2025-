
import math, pytest


def test_volume_cylinder():
    # volume = π * (d/2)^2 * h
    assert volume_cylinder(2, 2) == pytest.approx(math.pi * 1**2 * 2)  # diameter 2 -> radius 1
    assert volume_cylinder(0.2, 4) == pytest.approx(math.pi * 0.1**2 * 4)
    assert volume_cylinder(4, 1) == pytest.approx(math.pi * 2**2 * 1)
    
def test_area_cylinder():
    # area = 2πr * h + 2πr^2 = 2π*(d/2)*h + 2π*(d/2)^2
    assert area_cylinder(2, 2) == pytest.approx(2 * math.pi * 1 * 2 + 2 * math.pi * 1**2)
    assert area_cylinder(0.2, 4) == pytest.approx(2 * math.pi * 0.1 * 4 + 2 * math.pi * 0.1**2)
    assert area_cylinder(4, 1) == pytest.approx(2 * math.pi * 2 * 1 + 2 * math.pi * 2**2)
