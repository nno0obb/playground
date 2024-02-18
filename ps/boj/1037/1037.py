"""
# BOJ
# No. 1037
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    D = list(map(int, input().split()))

    # Logic
    D.sort()
    if N % 2 == 1:
        ans = D[N//2]**2
    else:
        ans = D[0] * D[-1]

    # Output
    print(ans)


if __name__ == '__main__':
    main()
