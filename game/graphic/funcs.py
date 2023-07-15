import random
import time
import functools
import os


def show_floating_stars():
    message = "Congratulations, You're the Winner!"
    stars = ['✨', '★', '✪', '✯', '✰']

    # Terminal dimensions
    terminal_width = 80
    terminal_height = 25

    while True:
        # Generate random positions for stars
        positions = [(random.randint(0, terminal_width), random.randint(0, terminal_height)) for _ in range(20)]
        
        # Clear the terminal screen
        print("\033c", end='')
        
        # Print stars and message
        for y in range(terminal_height):
            for x in range(terminal_width):
                if (x, y) in positions:
                    print(random.choice(stars), end='')
                else:
                    print(' ', end='')
            print()
        
        # Print the message at the center of the screen
        message_length = len(message)
        padding = ' ' * ((terminal_width - message_length) // 2)
        print(padding + message)
        input()
        
        # Pause for a short time
        time.sleep(0.2)


def show_sad_face():
    face = r"""
         .--------.
       .'          '.
      /   ~     ~    \
     :                :
     |       |        |   
     :                :
      \    _____     /
       '.          .'
         '--------'
    """
    message = "You lost..."

    # Clear the terminal screen
    print("\033c", end='')

    # Print the sad face
    print(face)
    
    # Print the message at the center of the screen
    message_length = len(message)
    padding = ' ' * ((80 - message_length) // 2)
    print(padding + message)


def slow_down(func):
    """Sleep 2 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper_slow_down


def separator(func):
    @functools.wraps(func)
    def print_line(*args, **kwargs):
        func(*args, **kwargs)
        print("_"*40)
    return print_line


def show_map(player: tuple, dimensions: int) -> str:
    game_map = " _ " * dimensions + "\n"
    for col in range(dimensions):
        for row in range(dimensions):
            if (row + 1, col + 1) == player:
                game_map += "|X|"
            else:
                game_map += "|_|"
        game_map += "\n"
    return game_map



def show_visited_cells(visited_cells: list[tuple], dimensions: int) -> str:
    game_map = " _ " * dimensions + "\n"
    for col in range(dimensions):
        for row in range(dimensions):
            if (row + 1, col + 1) in visited_cells:
                game_map += "|x|"
            else:
                game_map += "|_|"
        game_map += "\n"
    return game_map


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')

@separator
def show_welcome(name: str) -> str:
    welcome_str = f"""

                                    ****Dungeons & Dragons****

    Hello {name}! welcome to D&D game!! :)
    When the game starts, you will be thrown into the dragons world!
    Yes! there are some dragons!
    and you have to escape from them!
    But don't worry there is a way out and you have too find the door before the dragon finds you!

    you can play this game in 2 ways:
    default: 4x4 map
    custom: you can enter the dimensions of the map

    now just enter what you wish and the game will start...
    Good luck {name}!!

    *you can see help any time, just enter 'help'
    """
    print(welcome_str)


@separator
def show_help() -> str:
    help_str = """
    > start:
    > stop:
    > jump:
    > hint:
    > moves:
    > dragon smelling:
    > dragon seeing:
    > help:
    """
    print(help_str)