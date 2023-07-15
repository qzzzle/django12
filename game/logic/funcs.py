import logging
import random

from itertools import product

logger = logging.getLogger(__name__)

def get_locations(cells: list[tuple]) -> tuple:
    logger.debug(f"getting 3 random location from: {cells}")
    return random.sample(cells, k=3)


def generate_cells(dimensions: int) ->list[tuple]:
    logger.debug(f"generating cells by dimension: {dimensions}")
    side = range(1, dimensions+1)
    cells = [p for p in product(side, repeat=2)]
    return cells


def get_moves(player_location: tuple, dimensions: int) -> list :
    logger.debug(f"--getting available moves-- player location:{player_location}  map dimensions:{dimensions}x{dimensions}")
    moves = ["up", "down", "right", "left"]
    x, y = player_location
    if x == 1 :
        moves.remove("left")
    if x == (dimensions):
        moves.remove("right")
    if y == 1:
        moves.remove('up')
    if y == (dimensions):
        moves.remove("down")
    return moves


def move_character(location: tuple, move: str):
    logger.debug(f"--player moves-- from:{location} to {move}")
    x, y = location
    if move == "up":
        y -= 1
    elif move == "down":
        y += 1
    elif move == "right":
        x += 1
    elif move == "left":
        x -= 1
    new_location = (x, y)
    return new_location


def calculate_distance(first_cell: tuple, second_cell: tuple) -> float:
    x_1, y_1 = first_cell
    x_2, y_2 = second_cell
    x= pow((x_1 - x_2), 2)
    y= pow((y_1 - y_2), 2)
    distance = pow((x+y), 0.5)
    return distance


def can_dragon_smell(distance: float, smelling_power: float) -> bool:
    if distance <= smelling_power:
        return True
    else:
        return False


def can_dragon_see(distance: float, seeing_power: float) -> bool:
    if distance <= seeing_power:
        return True
    else:
        return False


def dragon_move(player: tuple, dragon: tuple) -> tuple:
    player_x, player_y = player
    dragon_x, dragon_y = dragon
    x = dragon_x - player_x
    y = dragon_y - player_y
    moves = []
    if x > 0:
        moves.append("left")
    elif x < 0:
        moves.append("right")
    if y > 0:
        moves.append("up")
    elif y < 0:
        moves.append("down")
    move = random.sample(moves, k=1)
    return move[0]


def jump_character(origin: tuple, destination:tuple, cells: list[tuple]) -> tuple[tuple, bool]:
    jump = False
    if destination in cells:
        jump = True
        return destination, jump
    elif destination not in cells:
        print("you should enter a valid cell! ")
        return origin, jump
    elif origin == destination:
        print("you can not jump in you current cell!")
        return origin, jump


def calculate_points(player_steps: int, hint_times: int) -> int:
    points = (player_steps * 10) - (hint_times * 25)
    return points


def get_hint(points: int):
    if points > 25:
        return True
    else:
        print("you don't have enough points to get hint")
        return False


