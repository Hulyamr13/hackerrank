# Complete the solve function below.
def solve(s):
    # Capitalize the first letter of each word and return the modified string
    return ' '.join(word.capitalize() for word in s.split())


if __name__ == '__main__':
    s = input().strip()
    result = solve(s)
    print(result)
