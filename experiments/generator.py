# Always wondered how generator works
# Try running it and see the magic behind it

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen = (i for i in lst)
print(gen)
# print(list(gen)) # Generator only generate once
lst[5] = 39
print(list(gen))
