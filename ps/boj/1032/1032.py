"""
# BOJ
# No. 1005
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    F = []
    for _ in range(N):
        filename = input()
        F.append(filename)

    # Logic
    for i in range(1, N):
        F[0] = ''.join(list(map(lambda x, y: x if x == y else '?', F[0], F[i])))

    ans = ''.join(F[0])

    # Output
    print(ans)


if __name__ == '__main__':
    main()
