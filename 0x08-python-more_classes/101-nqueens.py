#!/usr/bin/python3
"""N Queens"""
import sys


def print_error_and_exit(msg="", status=1):
    """Prints an error and exit with status"""
    print(msg)
    sys.exit(status)


def check_usage():
    """Checks and prints usage"""
    if len(sys.argv) != 2:
        print_error_and_exit("Usage: nqueens N")


def get_n() -> int:
    """Get number of queens from arguments"""
    try:
        n = int(sys.argv[1])
        if n < 4:
            print_error_and_exit("N must be at least 4")
        return n
    except Exception:
        print_error_and_exit("N must be a number")


def queens(n, i, a, b, c):
    """Generator for nqueens problem"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if __name__ == "__main__":
    check_usage()
    N = get_n()
    for solution in queens(N, 0, [], [], []):
        print([[x, solution[x]] for x in range(N)])
