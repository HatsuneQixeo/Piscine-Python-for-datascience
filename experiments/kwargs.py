def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(*args)
    print(*kwargs)
    print(*kwargs.keys())
    print(*kwargs.values())
    print({**kwargs})

func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     a='Apple', b='Bird', c='Cow', d='Donkey', e='Elephant')
