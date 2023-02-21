from src.utils import utils_print, utils_print_two
from src.utils_two import utils_print_tree
import sys


if __name__ == '__main__':
    arg = sys.argv[1]
    msg_one = utils_print.print_one(arg)
    msg_two = utils_print_two.print_two(arg)
    msg_tree = utils_print_tree.print_tree(arg)
    print(msg_one)
    print(msg_two)
    print(msg_tree)
    print(sys.path)
