import re

def validate_pan_number(pan):
    pattern = r'^[A-Z]{5}\d{4}[A-Z]$'
    if re.match(pattern, pan):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        pan_number = input().strip()
        print(validate_pan_number(pan_number))
