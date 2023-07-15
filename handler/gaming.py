from helper.consts import (
    GAMING,
    EXIT_COMMANDS,
    SEEING_POWER,
    SMELLING_POWER
    )

from game.logic.funcs import(
    get_locations,
    get_moves,
    calculate_distance,
    calculate_points,
    can_dragon_see,
    can_dragon_smell,
    dragon_move,
    move_character,
    get_hint,
    jump_character
)

from game.graphic.funcs import(
    show_map,
    clear_screen,
    show_visited_cells,
    show_floating_stars,
    show_sad_face,
    show_help
)

from .custom_setting import custom
from .default_setting import default


def gaming(game_setting):
    cells, dimensions = game_setting()
    player, dragon , door = get_locations(cells)
    visited_cells = [player]
    player_steps = len(visited_cells) - 1 
    hint_times = 0
    GAMING = True
    while GAMING:
        valid_moves = get_moves(player, dimensions)
        points = calculate_points(player_steps , hint_times)
        print(f"you are in room: {player}, points = {points}")
        print(f"dragon room: {dragon}") #pak beshe
        print(show_map(player, dimensions))
        print(f"you can move in: {valid_moves}")
        command = input("Please Enter your move: ").lower()
        if command in valid_moves:
            clear_screen()
            move = command
            player = move_character(player, move)
            visited_cells.append(player)
            player_steps = len(visited_cells)
            dragon_player_distance  = calculate_distance(dragon, player)
            if can_dragon_see(dragon_player_distance, SEEING_POWER):
                move = dragon_move(player, dragon)
                dragon = move_character(dragon, move)
                print(f"Now Dragon saw you and took a step to '{move}' towards you!")
                print(f"dragon room: {dragon}") #pak beshe
            elif can_dragon_smell(dragon_player_distance, SMELLING_POWER):
                print("dragon is smelling you! ")
                print("that means at least it is at least 3 steps away from you!")

            if player == dragon:
                show_sad_face()
                GAMING = False
            elif player == door:
                show_floating_stars()
                GAMING = False
        elif command in EXIT_COMMANDS:
            GAMING = False
        elif command == "hint":
            if get_hint(points):
                hint_strategy = input("jump or show visited cells?")
                if hint_strategy == "jump":
                    destination = input("jump to which cell? ")
                    destination = tuple(map(int, destination.split()))
                    # destination = destination.split()
                    # destination = tuple(int(destination[0]), int(destination[1]))
                    print(destination)
                    player, jump = jump_character(player, destination, cells)
                    if jump:
                        hint_times += 1
                        print("you jumped!")
                        print(show_map(player, dimensions))
                    
                elif hint_strategy == "show":
                    print(show_visited_cells(visited_cells, dimensions))
                    hint_times += 1
                else:
                    print("Please enter a valid command!")
        elif command =="help":
            show_help()
        else:
            print("Please enter a valid move!")