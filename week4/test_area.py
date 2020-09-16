## need this every time... i think?
from unittest import TestCase
## import py file in the directory
import area

class TestShapeAreas(TestCase):
    def test_triangle_area(self):
        # a trianlge with a heaight of 4 and a base of 5 should have an area of 10
        self.assertEqual(10, area.triangle_area(4,5))