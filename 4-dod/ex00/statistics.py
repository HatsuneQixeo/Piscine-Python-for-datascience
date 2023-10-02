def _get_mean(lst: list[int | float]) -> float:
    """Calculate mean in the given list of numbers"""

    return sum(lst) / len(lst)


def _get_median(lst: list[int | float]) -> int | float:
    """Calculate median in the given list of numbers"""

    length = len(lst)
    lst = sorted(lst)
    mid = length // 2
    median = lst[mid]
    if length % 2 == 0:
        median = (lst[mid - 1] + median) / 2
    return median


def _get_variance(lst: list[int | float]) -> float:
    """Calculate variance in the given list of numbers"""

    mean = _get_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def _get_quartile(lst: list[int | float]) -> list[int | float]:
    """Return the first and third quartile of the given list of numbers"""

    length = len(lst)
    lst = sorted(lst)
    return [lst[length // 4], lst[3 * length // 4]]


def _get_standard_deviation(lst: list[int | float]) -> float:
    """Calutate standard deviation in the given list of numbers"""

    return _get_variance(lst) ** .5


def ft_statistics(*args, **kwargs) -> None:
    if len(args) == 0:
        print('ERROR\n' * len(kwargs), end='')
        return
    for act in kwargs.values():
        match act:
            case 'mean':
                print('mean:', _get_mean(args))
            case 'median':
                print('median:', _get_median(args))
            case 'quartile':
                print('quartile:', _get_quartile(args))
            case 'std':
                print('std:', _get_standard_deviation(args))
            case 'var':
                print('var:', _get_variance(args))
