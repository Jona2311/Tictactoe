tic = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def g():
    try:
        global tic
        print("   0  1  2")
        for index, c in enumerate(tic):
            print(index, c)

        while True:
            player = int(input("Who is playing? 1 or 2: "))
            row = int(input("Which row are you playing? 0, 1 or 2: "))
            col = int(input("Which col are you playing? 0, 1 or 2: "))

            if player not in [1, 2] or row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("invalid input")
                continue
            if tic[row][col] == 0:
                tic[row][col] = player
                winner = win(tic)
                if winner != 0:
                    print(f"player {winner} wins!!!")
                    reset()
                    print("game reset")
                    break
                break
            else:
                print("Position taken, please try another")
    except Exception as c:
        print(f"sumn aint right, {c}")


def win(game):
    for row in game:
        if all(items == row[0] and row[0] != 0 for items in row):
            print(f"player {row[0]} wins horizontally!!!!")

    for col in range(len(game)):
        if all(row[col] == game[0][col] and game[0][col] != 0 for row in game):
            print(f"player {game[0][col]} wins vertically!!!!")

    if all(
        game[col][col] == game[0][0] and game[0][0] != 0 for col in range(len(game))
    ):
        print(f"player {game[0][0]} wins diagonally!!!!")

    if all(
        game[col][len(game) - col - 1] == game[0][len(game) - 1]
        and game[0][len(game) - 1] != 0
        for col in range(len(game))
    ):
        print(f"player {game[0][len(game) - 1]} wins diagonally!!!!")

    return 0


def reset():
    global tic
    print("resetting board....")
    tic = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


while True:
    g()
