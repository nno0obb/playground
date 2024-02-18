"""
# BOJ
# No. 10989
# Python 3.10.4
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(sys.stdin.readline())
    D = [0] * (10_000 + 1)
    for _ in range(N):
        n = int(sys.stdin.readline())

        # Logic
        D[n] += 1

    for i in range(1, 10_000+1):
        if D[i] == 0:
            continue

        # Output
        for _ in range(D[i]):
            print(i)


if __name__ == '__main__':
    main()
