import unittest

from classes.shape import shape
from classes.shape_strategy import *

class TestShape(unittest.TestCase):
    def setUp(self):
        self.s = shape().get_shape(shape_strategy= S_strategy())
        self.z = shape().get_shape(shape_strategy= Z_strategy())
        self.i = shape().get_shape(shape_strategy= I_strategy())
        self.o = shape().get_shape(shape_strategy= O_strategy())
        self.j = shape().get_shape(shape_strategy= J_strategy())
        self.l = shape().get_shape(shape_strategy= L_strategy())
        self.t = shape().get_shape(shape_strategy= T_strategy())

    def test_s_initial_values(self):
        self.assertEqual(self.s.name, "S")
        self.assertEqual(self.s.colour, (0, 255, 0))
        self.assertEqual(self.s.x, 5)
        self.assertEqual(self.s.y, 0)
        self.assertEqual(self.s.rotation, 0)

    def test_z_initial_values(self):
        self.assertEqual(self.z.name, "Z")
        self.assertEqual(self.z.colour, (255, 0, 0))
        self.assertEqual(self.z.x, 5)
        self.assertEqual(self.z.y, 0)
        self.assertEqual(self.z.rotation, 0)

    def test_i_initial_values(self):
        self.assertEqual(self.i.name, "I")
        self.assertEqual(self.i.colour, (0, 255, 255))
        self.assertEqual(self.i.x, 5)
        self.assertEqual(self.i.y, 0)
        self.assertEqual(self.i.rotation, 0)

    def test_o_initial_values(self):
        self.assertEqual(self.o.name, "O")
        self.assertEqual(self.o.colour, (255, 255, 0))
        self.assertEqual(self.o.x, 5)
        self.assertEqual(self.o.y, 0)
        self.assertEqual(self.o.rotation, 0)

    def test_j_initial_values(self):
        self.assertEqual(self.j.name, "J")
        self.assertEqual(self.j.colour, (255, 165, 0))
        self.assertEqual(self.j.x, 5)
        self.assertEqual(self.j.y, 0)
        self.assertEqual(self.j.rotation, 0)

    def test_l_initial_values(self):
        self.assertEqual(self.l.name, "L")
        self.assertEqual(self.l.colour, (0, 0, 255))
        self.assertEqual(self.l.x, 5)
        self.assertEqual(self.l.y, 0)
        self.assertEqual(self.l.rotation, 0)


if __name__ == '__main__':
    unittest.main()