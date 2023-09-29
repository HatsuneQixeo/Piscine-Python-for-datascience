TARGET_PERFECT = "Hatsune Miku is cute"
TARGET_TUPLE = tuple(TARGET_PERFECT.split())
TARGET_OFFCASE = TARGET_PERFECT.lower()
PROMPT = f'Enter ({TARGET_PERFECT}): '
MAX_PATIENCE = 4


streak = 0
patience = MAX_PATIENCE


def reset(msg: str):
    global streak
    global patience

    patience = min(streak, MAX_PATIENCE)
    streak = 0
    print(msg)


def increment(msg: str):
    global streak
    global patience

    streak += 1
    patience = min(patience + 1, MAX_PATIENCE)
    print(msg)


def decrement(msg: str):
    global patience
    global streak

    if patience != 0:
        patience -= 1
    elif streak != 0:
        reset('Ran out of patience!')
        return
    print(msg)


def input_matching(input: str):
    lst = tuple(input.split())
    # Either only space or case is off
    if (input.lower() == TARGET_OFFCASE) ^ (lst == TARGET_TUPLE):
        increment('Good!')
    else:
        match = sum(a.lower() == b.lower() for a, b in zip(lst, TARGET_TUPLE))
        if match == 0:
            reset('What a mess')
        elif match < len(TARGET_TUPLE) / 2:
            decrement('Try again!')
        else:
            decrement('Almost there')


while True:
    try:
        string = input(PROMPT)
        if len(string) < len(TARGET_PERFECT) / 8:
            reset("Are you even trying?")
        elif string == TARGET_PERFECT:
            increment('Perfect!')
        else:
            input_matching(string)
    except KeyboardInterrupt:
        print()
        continue
    except EOFError:
        exit(0)
    print('Current streak:', streak)
