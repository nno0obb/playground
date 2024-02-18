"""
# BOJ
# No. 1110
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    curr, ans = N, 0
    while ans == 0 or curr != N:
        prev = curr
        curr = prev % 10 * 10 + (prev % 10 + prev // 10) % 10
        ans += 1

    # Output
    print(ans)


if __name__ == '__main__':
    main()
