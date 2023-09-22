import numpy as np


# Invalid solution
# Rotates the inner structure more than outer border
def rotate_impl(matrix: np.ndarray[(int, int)], call: int):
    tmp = matrix[call][call]
    y_len = matrix.shape[0] - call - 1
    x_len = matrix.shape[1] - call - 1
    if y_len == 1 or x_len == 1:
        return matrix
    for i in range(call, x_len):
        matrix[call][i] = matrix[call][i + 1]
    for i in range(call, y_len):
        matrix[i][x_len] = matrix[i + 1][x_len]
    for i in range(x_len, call, -1):
        matrix[y_len][i] = matrix[y_len][i - 1]
    for i in range(y_len, call, -1):
        matrix[i][call] = matrix[i - 1][call]
    matrix[call + 1][call] = tmp
    return rotate_impl(matrix, call + 1)


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    buffer = np.array(matrix)
    if buffer.size == 0:
        return matrix
    return rotate_impl(buffer, 0).tolist()


def main():
    # matrix = [
    #     [1, 2],
    #     [3, 4]
    # ]
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     [10, 11, 12]
    # ]
    # 4 x 4 matrix
    # matrix = np.array([
    #     [ 1,  2,  3,  4],
    #     [12, 13, 14,  5],
    #     [11, 16, 15,  6],
    #     [10,  9,  8,  7]
    # ])
    matrix = np.array([
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    # 5 x 5 matrix
    # matrix = np.array([
    #     [ 1,  2,  3,  4,  5],
    #     [ 6,  7,  8,  9, 10],
    #     [11, 12, 13, 14, 15],
    #     [16, 17, 18, 19, 20],
    #     [21, 22, 23, 24, 25]
    # ])
    # print(matrix)
    # r90 = matrix
    # for _ in range(4):
    #     r90 = rotate(r90)
    # print(r90)
    # r180 = r90
    # for _ in range(4):
    #     r180 = rotate(r180)
    # print(r180)
    print(matrix)
    # print(matrix.T)


if __name__ == "__main__":
    main()
