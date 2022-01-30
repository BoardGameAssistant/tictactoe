import cv2

from gamevalidator import validate_conditions
from gameboard import Gameboard
from engine import GameEngine


def pipeline(image_path: str = "images/small_one_cross.jpg"):

    image = cv2.imread(image_path)
    gameboard = Gameboard.detect_game_board(image, debug=0)
    status = gameboard.status()
    print(status)
    cnt, status_bool = validate_conditions(status)
    if status_bool is False:
        return "Game is not valid, since somebody is cheating!"

    if cnt.get("X", 0) < cnt.get("O", 0):
        output = []
        ge = GameEngine(currentplayer="O", debug=0)
        board_output, is_game_finished, winner = ge.start(gameboard_file=image_path)
        if is_game_finished:
            if winner == "A TIE!":
                output.append("GAME OVER! IT WAS A TIE!")
            else:
                output.append(f"GAME OVER! THE WINNER IS {winner}!")
        else:
            output.append(board_output)
        return output
    elif cnt.get("X", 0) > cnt.get("O", 0):
        output = []
        ge = GameEngine(currentplayer="X", debug=0)
        board_output, is_game_finished, winner = ge.start(gameboard_file=image_path)
        if is_game_finished:
            if winner == "A TIE!":
                output.append("GAME OVER! IT WAS A TIE!")
            else:
                output.append(f"GAME OVER! THE WINNER IS {winner}!")
        else:
            output.append(board_output)
        return output
    else:
        output = []
        ge = GameEngine(currentplayer="X", debug=0)
        board_output, is_game_finished, winner = ge.start(gameboard_file=image_path)
        if is_game_finished:
            if winner == "A TIE!":
                output.append("GAME OVER! IT WAS A TIE!")
            else:
                output.append(f"GAME OVER! THE WINNER IS {winner}!")
        else:
            output.append(board_output)
        ge = GameEngine(currentplayer="O", debug=0)
        board_output, is_game_finished, winner = ge.start(gameboard_file=image_path)
        if is_game_finished:
            if winner == "A TIE!":
                output.append("GAME OVER! IT WAS A TIE!")
            else:
                output.append(f"GAME OVER! THE WINNER IS {winner}!")
        else:
            output.append(board_output)
        return output

print(pipeline(image_path = "images/one_average_x.jpg"))