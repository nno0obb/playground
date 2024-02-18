"""
# BOJ
# No. 2309
# Python 3.10.4
# by "nno0obb"
"""

import sys
from itertools import combinations


def main():
    # Input
    H = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))

    # Logic
    for comb in combinations(H, 2):
        if sum(H) - sum(comb) == 100:
            h1, h2 = comb
            H.remove(h1)
            H.remove(h2)
            break

    # Output
    ans = '\n'.join(map(str, sorted(H)))
    print(ans)


if __name__ == '__main__':
    main()
