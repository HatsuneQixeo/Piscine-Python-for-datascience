# import os


def log(progress: int, total_iteration: int, bar_capacity: int) -> None:
    """Print a progress bar to the stdout."""
    percentage = str(int(progress / total_iteration * 100)).rjust(3)
    iteration = str(progress).rjust(len(str(total_iteration)))
    bar_length = int(progress / total_iteration * bar_capacity)
    bar = str().ljust(bar_length, '█').ljust(bar_capacity)
    print(f"\r{percentage}%|{bar}| {iteration}/{total_iteration}", end='')


def getTermSize() -> int:
    """Return terminal size. Commented out due to os module not available."""
    # if os.isatty(1) is False:
    #     return os.get_terminal_size().columns
    return 80


def ft_tqdm(lst: range) -> None:
    """Initial call sets a goal, \
that is advanced each time the function is called.
Prints a progress bar to stdout each call."""

    total_iteration = len(lst)
    bar_capacity = getTermSize() - (len(str(total_iteration)) * 2) - 5 - 3
    # 5 is the total literal character count, 3 is progress percentage
    for i in range(total_iteration):
        log(i, total_iteration, bar_capacity)
        yield
    log(total_iteration, total_iteration, bar_capacity)
    print()
