# from . import utils_print
# from ..utils_two import utils_print_tree
from src.utils import utils_print
from src.utils_two import utils_print_tree


def print_two(word: str) -> str:
    msg = utils_print.print_one(word)
    msg_two = utils_print_tree.print_tree(msg)
    return f'print two: {msg_two} inside'
