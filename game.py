def check_move(x, arrRep, validRowValue, playerNumber):
    allowed = True

    if validRowValue[x] >= 6:
        allowed = False

    rowNumber = validRowValue[x]

    if allowed:
        arrRep[validRowValue[x]][x] = playerNumber

        validRowValue[x] += 1

    return allowed, rowNumber


def game_over(arrRep, agent_number, opponent_number, current_column, legalRowNumber):
    isWinningMove = victory(arrRep, agent_number)

    if isWinningMove == 1:

        return agent_number, isWinningMove

    else:

        isWinningMove = victory(arrRep, opponent_number)

    if isWinningMove == 1:
        return opponent_number, isWinningMove


def victory(arrayRep, x):
    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if j == 3:

                    if (arrayRep[i][j + 1] == x and arrayRep[i][j + 2] == x and arrayRep[i][j + 3] == x) or (
                                        arrayRep[i][j - 1] == x and arrayRep[i][j - 2] == x and arrayRep[i][
                                    j - 3] == x):
                        print "x wins", x

                        return 1

                elif j < 3:

                    if (arrayRep[i][j + 1] == x and arrayRep[i][j + 2] == x and arrayRep[i][j + 3] == x):
                        print "x wins", x

                        return 1

                elif (arrayRep[i][j - 1] == x and arrayRep[i][j - 2] == x and arrayRep[i][j - 3] == x):

                    print "x wins", x

                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if i <= 2:

                    if (arrayRep[i + 1][j] == x and arrayRep[i + 2][j] == x and arrayRep[i + 3][j] == x):
                        print "x wins", x

                        return 1

                elif (arrayRep[i - 1][j] == x and arrayRep[i - 2][j] == x and arrayRep[i - 3][j] == x):

                    print "x wins", x

                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                print "x2"

                if i <= 2 and j <= 3:

                    print "A"

                    print i, j

                    if (arrayRep[i + 1][j + 1] == x and arrayRep[i + 2][j + 2] == x and arrayRep[i + 3][j + 3] == x):
                        print "x wins", x

                        return 1

                if i <= 2 and j >= 3:

                    print "B"

                    print i, j

                    if (arrayRep[i + 1][j - 1] == x and arrayRep[i + 2][j - 2] == x and arrayRep[i + 3][j - 3] == x):
                        print "x wins", x

                        return 1

                if i >= 3 and j >= 3:

                    print "C"

                    print i, j

                    if (arrayRep[i - 1][j - 1] == x and arrayRep[i - 2][j - 2] == x and arrayRep[i - 3][j - 3] == x):
                        print "x wins", x

                        return 1

                if i >= 3 and j <= 3:

                    print "D"

                    print i, j

                    if (arrayRep[i - 1][j + 1] == x and arrayRep[i - 2][j + 2] == x and arrayRep[i - 3][j + 3] == x):
                        print "x wins", x

                        return 1

    return 0