import numpy as np

arr = np.array([
    [
        [ 1,  2,  3],
        [ 4,  5,  6]
    ],
    [
        [ 7,  8,  9],
        [10, 11, 12]
    ]
])

print('arr:', arr)

for i in range(3):
    print(f"mean axis={i}:\n{arr.mean(dtype=int, axis=i)}")

for i in range(5):
    print(f"dot({i}):\n{np.dot(arr[..., :2], [i, i])}")

print()
print(arr[..., 1])

arr = np.array([1, 2, 3])

arr[:2] = [0, 1]
print(arr)

arr[:] = [0]
print(arr)

arr[:] = 1
print(arr)
