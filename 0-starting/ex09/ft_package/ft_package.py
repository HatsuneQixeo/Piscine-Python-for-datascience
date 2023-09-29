def count_in_list(iterable, element):
    """Return the amount of duplicates of element in iterable."""
    return sum(1 for i in iterable if i == element)
