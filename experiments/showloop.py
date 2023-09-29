iteration = range(1, 100)

for i in iteration:
	lst = list(range(i))
	print('i:          ', i)
	print('3quarter:   ', i // 4 * 3, lst[i // 4 * 3])
	print('half+quarter', i // 2 + i // 4, lst[i // 2 + i // 4])
	# print('len-quarter ', i - i // 4, lst[i - i // 4])
	print('len*.75	 ', i * .75, lst[int(i * .75)])
	print()
