import unittest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from src.utils import utils_print
from src.utils import utils_print_two
from src.utils_two import utils_print_tree


class TestPrint(unittest.TestCase):
    def test_print_one(self):
        msg = utils_print.print_one('test')
        self.assertEqual(msg, 'print one: test')

    def test_print_two(self):
        msg = utils_print_two.print_two('test')
        self.assertEqual(msg, 'print two: print tree: print one: test inside')

    def test_print_tree(self):
        msg = utils_print_tree.print_tree('test')
        self.assertEqual(msg, 'print tree: test')


if __name__ == '__main__':
    unittest.main()
