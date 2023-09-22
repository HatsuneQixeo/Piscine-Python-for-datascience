def	log(a, b):
	print(hex(id(a)))
	print(hex(id(b)))
	print("a:", a)
	print("b:", b)
	print("a is b:", a is b)

a = "Hatsune Miku"
b = a
log(a, b)
b = b.capitalize()
log(a, b)
b = "Hatsune Miku"
log(a, b)
b = b.capitalize()
a = a.capitalize()
log(a, b)
