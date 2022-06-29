import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It is a tie between you and computer."

    if is_win(user, computer):
        return "Wow! You won."

    return "You lost!"


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())
