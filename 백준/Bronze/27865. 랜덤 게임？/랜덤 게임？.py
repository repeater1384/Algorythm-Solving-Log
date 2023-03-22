import sys

sys.stdin.readline()
while True:
    sys.stdout.write('? 1\n')
    sys.stdout.flush()
    result = sys.stdin.readline().rstrip()
    if result == 'Y':
        sys.stdout.write('! 1\n')
        sys.stdout.flush()
        break
