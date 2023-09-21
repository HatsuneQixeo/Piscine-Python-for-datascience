from array2D import slice_me


family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# import datetime

# lst = [39] * 100000
# start = datetime.datetime.now()
# slice_me(lst, 0, 80000)
# print((datetime.datetime.now() - start).total_seconds())
