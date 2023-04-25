def is_multiple_of_eight(n):
    """
    Checks if a given number is a multiple of 8.

    Args:
    - n: int, the number to be checked.

    Returns:
    - bool, True if n is a multiple of 8, False otherwise.
    """
    return n % 8 == 0


def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        print('Second' if is_multiple_of_eight(n) else 'First')


if __name__ == "__main__":
    main()
