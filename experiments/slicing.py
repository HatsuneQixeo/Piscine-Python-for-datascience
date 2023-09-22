lst = [
    [1, 2, 3],
    [4, 5, 6]
]

copy = lst[:] # returns a shallow copy (only copy first layer)
copy = lst[:][:] # Same as above
copy = [*lst[:][:]] # Same as above
copy = [*lst[:]] # Same as above

# copy[:][0] = 0  # Numpy array magic, : returns a copy for list, unlike ndarray which returns a view
# Hell, ndarray could even take in a tuple for indexing
copy[0][0] = 0
copy[1][0] = 0
print(lst)
print(copy)


lst = [1 ,2, 3]

copy = lst[:]

copy[0] = 0
print(lst)
print(copy)

# Conclusion: Numpy array is magic
# lst[None] = 0  # another numpy array magic
# print(lst[...])  # yet another numpy array magic
