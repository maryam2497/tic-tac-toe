
def box(arr):

    print("\t", arr[0][0], "\t|\t", arr[0][1], "\t|\t", arr[0][2])
    print("  ------|-------|-------")
    print("\t", arr[1][0], "\t|\t", arr[1][1], "\t|\t", arr[1][2])
    print("  ------|-------|-------")
    print("\t", arr[2][0], "\t|\t", arr[2][1], "\t|\t", arr[2][2])


def turn_check():
    turn = 1
    for i in range(9):
        turn = player_turn(turn)
        if (turn > 9):
            print("game over")


def player_turn(turn):
    if (turn % 2 == 0):
        print("player 2 turn")
        sign = "O"
        num = int(input("enter box num"))
        num = invalidNum(num)
        player(num, sign)
        turn += 1
        return turn

    else:
        print("player 1 turn")
        num = int(input("enter box num"))
        sign = "X"
        num = invalidNum(num)
        player(num, sign)
        turn += 1
        return turn


def invalidNum(num):
    if (num < 1 or num > 9):
        print("invalid number")
        num = int(input("enter box num again"))
        invalidNum(num)
    else:
        return num


def filledBox(sign):
    print("box already filled")
    num = int(input("Enter box num again"))
    player(num, sign)


def player(num, sign):
    if num == 1:
        if (arr[0][0] != 'O' and arr[0][0] != 'X'):
            arr[0][0] = sign
            winner(sign, arr)
            box(arr)
        else:
            filledBox(sign)
    else:
        if num == 2:
            if (arr[0][1] != 'O' and arr[0][1] != 'X'):
                arr[0][1] = sign
                winner(sign, arr)
                box(arr)
            else:
                filledBox(sign)
        else:
            if num == 3:
                if (arr[0][2] != 'O' and arr[0][2] != 'X'):
                    arr[0][2] = sign
                    winner(sign, arr)
                    box(arr)
                else:
                    filledBox(sign)
            else:
                if num == 4:
                    if (arr[1][0] != 'O' and arr[1][0] != 'X'):
                        arr[1][0] = sign
                        winner(sign, arr)
                        box(arr)
                    else:
                        filledBox(sign)
                else:
                    if num == 5:
                        if (arr[1][1] != 'O' and arr[1][1] != 'X'):
                            arr[1][1] = sign
                            winner(sign, arr)
                            box(arr)
                        else:
                            filledBox(sign)
                    else:
                        if num == 6:
                            if (arr[1][2] != 'O' and arr[1][2] != 'X'):
                                arr[1][2] = sign
                                winner(sign, arr)
                                box(arr)
                            else:
                                filledBox(sign)
                        else:
                            if num == 7:
                                if (arr[2][0] != 'O' and arr[2][0] != 'X'):
                                    arr[2][0] = sign
                                    winner(sign, arr)
                                    box(arr)
                                else:
                                    filledBox(sign)
                            else:
                                if num == 8:
                                    if (arr[2][1] != 'O' and arr[2][1] != 'X'):
                                        arr[2][1] = sign
                                        winner(sign, arr)
                                        box(arr)
                                    else:
                                        filledBox(sign)
                                else:
                                    if num == 9:
                                     if (arr[2][2] != 'O' and arr[2][2] != 'X'):
                                       arr[2][2] = sign
                                       winner(sign, arr)
                                       box(arr)
                                     else:
                                        filledBox(sign)


def winner(sign, arr):
    if (arr[0][0] == sign and arr[1][1] == sign and arr[2][2] == sign) or (
            arr[0][0] == sign and arr[1][0] == sign and arr[2][0] == sign) or (
            arr[0][1] == sign and arr[1][1] == sign and arr[2][1] == sign) or (
            arr[0][2] == sign and arr[1][2] == sign and arr[2][2] == sign) or (
            arr[0][0] == sign and arr[0][1] == sign and arr[0][2] == sign) or (
            arr[1][0] == sign and arr[1][1] == sign and arr[1][2] == sign) or (
            arr[2][0] == sign and arr[2][1] == sign and arr[2][2] == sign) or (
            arr[2][0] == sign and arr[1][1] == sign and arr[0][2] == sign):
        if (sign == "X"):
            box(arr)
            print("CONGRATS!!!  player 1 wins")
            exit()
        else:
            box(arr)
            print("CONGRATS!!!  player 2 wins")
            exit()


print("\tTIC TAC TOE")
print("player 1(X)")
print("player 2(O)")
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
box(arr)
turn_check()
