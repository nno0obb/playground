"""
# BOJ
# No. 1002
# Python 3.10.4
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        # Logic
        d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # dist
        r1, r2 = max(r1, r2), min(r1, r2)

        ans = None
        if r1 == r2:
            if d > (r1 + r2):
                ans = 0
            elif d == (r1 + r2):
                ans = 1
            elif 0 < d < (r1 + r2):
                ans = 2
            elif d == 0:
                ans = -1
        else:
            if d > (r1 + r2):
                ans = 0
            elif d == (r1 + r2):
                ans = 1
            elif (r1 - r2) < d < (r1 + r2):
                ans = 2
            elif (d + r2) == r1:
                ans = 1
            elif (d + r2) < r1:
                ans = 0

        # Output
        print(ans)


if __name__ == '__main__':
    main()
