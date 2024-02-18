"""
# BOJ
# No. 2775
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Logic
    # (a, b) = (a-1, 1) + (a-1, 2) + ... + (a-1, b)
    # (a, b) = (a, b-1) + (a-1, b)
    A = [[0 for _ in range(14+1)] for _ in range(14+1)]
    for i in range(1, 14+1):
        A[0][i] = i
    for i in range(1, 14+1):
        for j in range(1, 14+1):
            A[i][j] = A[i][j-1] + A[i-1][j]

    # Input
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())

        # Output
        print(A[k][n])


if __name__ == '__main__':
    main()
