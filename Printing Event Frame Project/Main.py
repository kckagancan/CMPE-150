car_height = int(input())
car_length = int(input())
man_height = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

space = 15
for frame in range(16 + car_length):

    # create new list
    event = [[] for i in range(8+man_height)]

    for i in range(len(event)):
        if (space + car_length >= 5):
            for j in range(space + car_length):
                event[i].append(' ')
        else:
            for j in range(5):
                event[i].append(' ')

    # create the man
    for i in range(5):
        event[0][i] = 'X'
    for i in range(1, 3):
        event[i][0] = 'X'
        event[i][4] = 'X'
    for i in range(5):
        event[3][i] = 'X'
    event[4][2] = 'X'
    for i in range(5):
        event[5][i] = 'X'
    for i in range(6, 6 + man_height):
        event[i][2] = 'X'
    event[6+man_height][1] = 'X'
    event[6+man_height][3] = 'X'
    event[7+man_height][0] = 'X'
    event[7+man_height][4] = 'X'

    # create the car
    outer_size = len(event)
    inner_size = space + car_length
    z = outer_size - 4

    for i in range(car_height):

        if (z == outer_size - 4 or z == outer_size - 3 - car_height):

            if space >= 0:
                for j in range(inner_size - 1, space - 1, -1):
                    event[z][j] = 'X'

            else:
                for j in range(inner_size - 1, -1, -1):
                    event[z][j] = 'X'

        else:

            if inner_size - 1 >= 0:
                event[z][inner_size - 1] = 'X'

            if space >= 0:
                event[z][space] = 'X'
                for l in range(inner_size - 2, space, -1):
                    event[z][l] = ' '

            if space < 0:
                for l in range(inner_size - 2, -1, -1):
                    event[z][l] = ' '

        z -= 1

    # print the list
    for k in range(len(event)):
        for j in range(len(event[k])):
            print(event[k][j], end='')
        print()

    print()
    space -= 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
