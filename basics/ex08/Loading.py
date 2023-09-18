import os


def log(progress: int, total_iteration: int, bar_capacity: int) -> None:
    percentage = str(int(progress / total_iteration * 100)).rjust(3)
    iteration = str(progress).rjust(len(str(total_iteration)))
    bar_length = int(progress / total_iteration * bar_capacity)
    bar = str().ljust(bar_length, '█').ljust(bar_capacity)
    print(f"\r{percentage}%|{bar}| {iteration}/{total_iteration}", end='')


def getTermSize() -> int:
    if os.isatty(1) is False:
        return 80
    return os.get_terminal_size().columns


def ft_tqdm(lst: range) -> None:
    total_iteration = len(lst)
    bar_capacity = getTermSize() - (len(str(total_iteration)) * 2) - 5 - 3
    # 5 is the total literal character count, 3 is progress percentage
    for i in lst:
        log(i, total_iteration, bar_capacity)
        yield
    log(total_iteration, total_iteration, bar_capacity)
    print()
