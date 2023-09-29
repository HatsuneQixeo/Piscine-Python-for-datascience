from callLimit import callLimit


@callLimit(3)
def f():
    """f"""

    print("f()")


@callLimit(1)
def g():
    """g"""

    print("g()")


for i in range(3):
    f()
    g()
