"""
# BOJ
# No. 1157
# Python 3.10.4
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    W = input()

    # Logic
    c1 = Counter(W.upper())
    c2 = Counter(c1.values())

    if c2[max(c1.values())] > 1:
        ans = '?'
    else:
        ans, count = c1.most_common(1).pop()

    # Output
    print(ans)


if __name__ == '__main__':
    main()
