"""
# BOJ
# No. 2609
# Python 3.10.4
# by "nno0obb"
"""


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    ans = '\n'.join(map(str, [gcd(A, B), lcm(A, B)]))

    # Output
    print(ans)


if __name__ == '__main__':
    main()
