import re

def is_valid_username(username):
    pattern = r'^[_.]\d+[a-zA-Z]{0,}[_]?$'
    return bool(re.match(pattern, username))

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        username = input().strip()
        if is_valid_username(username):
            print("VALID")
        else:
            print("INVALID")
