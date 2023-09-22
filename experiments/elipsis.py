import numpy as np


def isSame(a: np.ndarray, b: np.ndarray, prefix = None) -> None:
    """Prints the shape of a and b.
    Displays == or != based on the result of np.array_equal(a, b)
    """

    if prefix is not None:
        print(f"{prefix}", end=': ')
    print(a.shape, '==' if np.array_equal(a, b) else '!=', b.shape)

# An array of 2 rows, 3 columns, 4 depth, for a clear repesentation of shape
arr = np.array([
    [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24],
    ],
], dtype=int)

print(arr.shape)
print('arr:', arr)
print()

# Basically, ... is a wildcard for any number of : (within it's indices)
# Does not allow duplicates,
# since that would create ambiguity for how many dimensions it should expand

isSame(arr[...], arr)
isSame(arr[...], arr[:])
isSame(arr[...], arr[:, :])
isSame(arr[...], arr[:, :, :])

# # (No reason to put elipsis or : at the end)
# isSame(arr[1], arr[1, :])
# isSame(arr[1], arr[1, ...])
# isSame(arr[1, :], arr[1, ...])

isSame(arr[1, ..., 1], arr[1, :, 1])
isSame(arr[..., 1], arr[:, :, 1])
isSame(arr[..., :1], arr[:, :, :1])
print()


# Please ignore the rest for the sake of your sanity
# Just don't use multiple subscript operator for np.ndarray



# # Muliple subscript operator
# isSame(arr[:, :], arr[:][:], 'arr[:, :], arr[:][:]')
# # isSame(arr[:][1], arr[:, 1], 'arr[:][1], arr[:, 1]')
# # print(arr[:][1]) # Returns the second row
# # print(arr[:, 1]) # Returns the second column of each row
# # isSame(arr[:][1], arr[1, :], 'arr[:][1], arr[1, :]') # IS SAME
# isSame(arr[:][1], arr[1], 'arr[:][1], arr[1]') # IS SAME
# # Does that mean the subscript operator is interpreted from right to left for np.ndarray?
# print()

# print("Comparing with arr[:][1]")
# rangerip = range(len(arr[1]))  # range(0, 3)
# tuplerip = tuple(rangerip)  # (0, 1, 2)
# print(f"Column, {rangerip}, {tuplerip}")
# isSame(arr[:][1], arr[1, :], '[1, colon]')
# isSame(arr[:][1], arr[1, tuplerip], '[1, tuple]')
# isSame(arr[:][1], arr[1, rangerip], '[1, range]')

# rangerip = range(len(arr))  # range(0, 2)
# tuplerip = tuple(rangerip)  # (0, 1)
# print(f"Row: {rangerip}, {tuplerip}")
# isSame(arr[:][1], arr[:, 1], '[colon, 1]')
# isSame(arr[:][1], arr[tuplerip, 1], '[tuple, 1]')
# isSame(arr[:][1], arr[rangerip, 1], '[range, 1]')
# print()

# # Tuple, colon, and range object don't get interpreted the same way
# # Tuple itself did not return anything?
# # Range and colon seem to be return the same thing
# isSame(arr[:][1], arr[tuplerip][1], '[tuple][1]')
# isSame(arr[:][1], arr[rangerip][1], '[range][1]')
# isSame(arr[:][1], arr[:][1], '[:][1]')

