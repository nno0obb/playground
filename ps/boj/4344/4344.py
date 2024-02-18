"""
# BOJ
# No. 4344
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    C = int(input())
    for _ in range(C):
        S = list(map(int, input().split()))

        # Logic
        N = S.pop(0)
        avg = sum(S) / N
        pct = len(list(filter(lambda x: x > avg, S))) / N * 100
        ans = f'{pct:.3f}%'

        # Output
        print(ans)


if __name__ == '__main__':
    main()
