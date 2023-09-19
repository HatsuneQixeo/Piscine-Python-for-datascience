import sys

if len(sys.argv) == 2:
    try:
        print(["I'm Even", "I'm Odd"][int(sys.argv[1]) % 2])
    except Exception:
        print("AssertionError: argument is not an integer")
        exit(1)
elif len(sys.argv) != 1:
    print("AssertionError: more than one argument is provided")
    exit(1)
