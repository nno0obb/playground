"""
# BOJ
# No. 1546
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = list(map(int, input().split()))

    # Logic
    ans = (sum(S) / max(S) * 100) / N

    # Output
    print(ans)


if __name__ == '__main__':
    main()
