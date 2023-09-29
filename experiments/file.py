import sys

# Yes, temporary object are cleaned up immediately after use

file = open(sys.argv[0], 'r')
print(open(sys.argv[0], 'r').fileno())
print(file=open(sys.argv[0], 'a'))
print(open('../clean.sh', 'r').fileno())
print(open(sys.argv[0], 'r').fileno())
print(open(sys.argv[0], 'r').fileno())
print(open(sys.argv[0], 'r').fileno())

