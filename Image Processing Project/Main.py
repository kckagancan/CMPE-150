inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def read_imagefile(f):
    img_matrix = []

    first_line = True
    for line in f:
        if first_line:

            first_line = False
            continue

        line_lst = line.strip().split()

        temp = []
        for num in line_lst:
            temp.append(int(num))

        img_matrix.append(temp)

    return img_matrix


def write_imagefile(f, img_matrix):

    CODE = "P2"
    WIDTH = len(img_matrix[0])
    HEIGHT = len(img_matrix)
    MAX_LEVEL = 255

    f.write(f"{CODE} {WIDTH} {HEIGHT} {MAX_LEVEL}\n")

    for i in range(HEIGHT):
        for j in range(WIDTH):

            f.write(str(img_matrix[i][j]))

            if j == WIDTH - 1:
                f.write("\n")
            else:
                f.write(" ")


def misalign(img_matrix):

    HEIGHT = len(img_matrix)

    for i in range(1, len(img_matrix[0]), 2):
        for j in range(HEIGHT//2):
            temp = img_matrix[j][i]
            img_matrix[j][i] = img_matrix[HEIGHT - 1 - j][i]
            img_matrix[HEIGHT - 1 - j][i] = temp

    return img_matrix


def sort_columns(img_matrix):

    for j in range(len(img_matrix[0])):
        temp = []
        for i in range(len(img_matrix)):
            temp.append(img_matrix[i][j])

        temp.sort()
        row = 0
        for num in temp:
            img_matrix[row][j] = num
            row += 1

    return img_matrix


def sort_rows_border(img_matrix):

    for i in range(len(img_matrix)):
        img_matrix[i].append(0)
        temp = []
        col_num = 0
        for j in range(len(img_matrix[i])):

            if img_matrix[i][j] == 0:

                temp.sort()
                for num in temp:
                    img_matrix[i][col_num] = num
                    col_num += 1

                col_num = j+1
                temp = []

            else:
                temp.append(img_matrix[i][j])

        img_matrix[i].pop()

    return img_matrix


def convolution(img_matrix, kernel):

    new_matrix = [[0 for i in range(len(img_matrix[0]))]
                  for j in range(len(img_matrix))]

    for i in range(len(img_matrix)):
        for j in range(len(img_matrix[0])):
            convolution_result = 0

            start_row = i-1
            start_col = j-1

            for p in range(3):
                for t in range(3):
                    if (start_row < 0 or start_row >= len(img_matrix)) or (start_col < 0 or start_col >= len(img_matrix[0])):
                        start_col += 1
                        continue

                    convolution_result += kernel[p][t] * \
                        img_matrix[start_row][start_col]
                    start_col += 1

                start_row += 1
                start_col = j-1

            if convolution_result > 255:
                new_matrix[i][j] = 255
            elif convolution_result < 0:
                new_matrix[i][j] = 0
            else:
                new_matrix[i][j] = convolution_result

    return new_matrix


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
