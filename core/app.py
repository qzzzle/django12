import logging
from getpass import getpass

from game.graphic.funcs import(
    show_welcome,
    clear_screen
)
from helper.consts import (
    RUNNING,
    SETTING,
    EXIT_COMMANDS,
)
from helper.commands import COMMANDS
from handler.gaming import gaming

logger = logging.getLogger(__name__)

def main():
    clear_screen()
    name = input("What is your name dear? ")
    clear_screen()
    show_welcome(name)
    
    while RUNNING:
        command = input('new game >> default/custom? ').lower()

        if command in EXIT_COMMANDS:
            break
        elif command in SETTING:
            game_setting = COMMANDS[command]
            gaming(game_setting)
            clear_screen()

        else:
            raise NotImplementedError()