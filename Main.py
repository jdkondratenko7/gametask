import click
from Objects import Board


@click.command()
@click.argument("cols", type=click.INT, default=7)
@click.argument("rows", type=click.INT, default=6)
@click.argument("to_win", type=click.INT, default=4)
@click.argument("num_players", type=click.INT, default=2)
def start_game(cols: int = 7, rows: int = 6, to_win: int = 4, num_players: int = 2):
    board = Board(cols, rows, to_win)
    board.draw()
    current_move = 1
    over = False
    while not over and board.has_empty():
        for player_ind in range(1, num_players + 1):
            print(f"Move {current_move}")
            col = int(input("Enter a column number to make a move: "))
            move = board.make_move(col % cols, player_ind)
            while move == -1:
                print("Impossible!")
                col = int(input("Please enter another column number to make a move: "))
                move = board.make_move(col, player_ind)
            board.draw()
            if move == 1:
                print('You won!')
                over = True
                break
            current_move += 1
    print("Game over!")


if __name__ == "__main__":
    start_game()
