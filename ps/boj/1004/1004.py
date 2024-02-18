"""
# BOJ
# No. 1004
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        C = [[0, 0, 0] for _ in range(n)]
        for i in range(n):
            cx, cy, r = map(int, input().split())
            C[i][:] = [cx, cy, r]

        # Logic
        ans = 0
        for i in range(n):
            cx, cy, r = C[i][:]
            p1 = (x1-cx)**2 + (y1-cy)**2 - r**2  # p1 > 0, out / p1 < 0, in
            p2 = (x2-cx)**2 + (y2-cy)**2 - r**2  # p2 > 0, out / p2 < 0, in
            if p1 * p2 < 0:
                ans += 1

        # Output
        print(ans)


if __name__ == '__main__':
    main()
