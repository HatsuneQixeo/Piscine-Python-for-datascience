import sys

sys.tracebacklimit = 0

len = len(sys.argv)
if len == 1:
    exit(0)
assert len == 2, "more than one argument is provided"

arg = sys.argv[1]
if arg[0] == '-' or arg[0] == '+':
    arg = arg[1:]
assert arg.isnumeric(), "argument is not an integer"

print(["I'm Even", "I'm Odd"][int(arg) % 2])
