import logging

from getpass import getpass
from helper.consts import DEFAULT_DIMENSIONS
from game.logic.funcs import (
    generate_cells,
    )


logger = logging.getLogger(__name__)


def custom():
    try:
        dimensions = int(input("Please Enter the dimensions of the map you want to generate:"))
    except ValueError as ve:
        print("Error: you should enter an integer!")
        getpass('>> to continue playing in default map which is 4x4 please Enter...')
        # print(">> or you can press q and start a new game ")
        logger.debug(f"user entered a non-integer as dimensions and the default_dimensions replaced")
        dimensions = DEFAULT_DIMENSIONS
    finally:
        cells = generate_cells(dimensions)
        return cells, dimensions