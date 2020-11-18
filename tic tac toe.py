def print_playground(x):
    print("---------")
    print("| {0} {1} {2} |".format(x[0], x[1], x[2]))
    print("| {0} {1} {2} |".format(x[3], x[4], x[5]))
    print("| {0} {1} {2} |".format(x[6], x[7], x[8]))
    print("---------")


def win_conditions(x):
    win0 = x[0] + x[1] + x[2]
    win1 = x[3] + x[4] + x[5]
    win2 = x[6] + x[7] + x[8]
    win3 = x[0] + x[3] + x[6]
    win4 = x[1] + x[4] + x[7]
    win5 = x[2] + x[5] + x[8]
    win6 = x[0] + x[4] + x[8]
    win7 = x[2] + x[4] + x[6]
    condition1 = win0 == "XXX" or win1 == "XXX" or win2 == "XXX" or win3 == "XXX" or win4 == "XXX" or win5 == "XXX" or win6 == "XXX" or win7 == "XXX"
    condition2 = win0 == "OOO" or win1 == "OOO" or win2 == "OOO" or win3 == "OOO" or win4 == "OOO" or win5 == "OOO" or win6 == "OOO" or win7 == "OOO"
    if condition1 == False and condition2 == False and "_" not in x:
        print("Draw")
        exit(0)

    elif condition1 == True:
        print("X wins")
        exit(0)

    elif condition2 == True:
        print("O wins")
        exit(0)


x = ["_","_","_","_","_","_","_","_","_"]
x = list(x)
print_playground(x)
condition = True
turn = True
error = ["1","2","3"]
while condition == True:
    coordinates = input("Enter the coordinates: ").split()
    if coordinates[0] not in error or coordinates[1] not in error:
        print("You should enter the numbers from 1 to 3!")
    else:
        a = int(coordinates[0])
        b = int(coordinates[1])

        if a == 1 and b == 1:
            if turn == False:
                if x[6] == "_":
                    x[6] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[6] == "_":
                    x[6] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 1 and b == 2:
            if turn == False:
                if x[3] == "_":
                    x[3] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[3] == "_":
                    x[3] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 1 and b == 3:
            if turn == False:
                if x[0] == "_":
                    x[0] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[0] == "_":
                    x[0] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 2 and b == 1:
            if turn == False:
                if x[7] == "_":
                    x[7] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[7] == "_":
                    x[7] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 2 and b == 2:
            if turn == False:
                if x[4] == "_":
                    x[4] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[4] == "_":
                    x[4] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 2 and b == 3:
            if turn == False:
                if x[1] == "_":
                    x[1] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[1] == "_":
                    x[1] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 3 and b == 1:
            if turn == False:
                if x[8] == "_":
                    x[8] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[8] == "_":
                    x[8] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 3 and b == 2:
            if turn == False:
                if x[5] == "_":
                    x[5] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[5] == "_":
                    x[5] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
        elif a == 3 and b == 3:
            if turn == False:
                if x[2] == "_":
                    x[2] = "O"
                    print_playground(x)
                    turn = True
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")
            elif turn == True:
                if x[2] == "_":
                    x[2] = "X"
                    print_playground(x)
                    turn = False
                    win_conditions(x)
                else:
                    print("This cell is occupied! Choose another one!")


