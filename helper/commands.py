from handler.custom_setting import custom
from handler.default_setting import default
from game.graphic.funcs import show_help
from game.logic.funcs import (
    get_hint,
    jump_character
)

COMMANDS = {
    "custom": custom,
    "default": default

}

# IN_GAME_COMMANDS = {
#     "hint": get_hint,
#     "jump": jump_character,
#     "help": show_help, 
#     }