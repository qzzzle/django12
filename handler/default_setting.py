from game.logic.funcs import generate_cells
from helper.consts import DEFAULT_DIMENSIONS


def default():
    dimensions = DEFAULT_DIMENSIONS
    cells = generate_cells(dimensions)
    return cells, dimensions