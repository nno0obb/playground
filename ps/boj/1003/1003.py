"""
# BOJ
# No. 1003
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Logic
    F = [0] * (41+1)
    F[0], F[1] = 1, 0
    for i in range(2, 41+1):
        F[i] = F[i-1] + F[i-2]

    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Output
        print(F[N], F[N+1])


if __name__ == '__main__':
    main()
