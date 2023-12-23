import re

def validate_id_number(id_number):
    pattern = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'
    if re.match(pattern, id_number):
        return "VALID"
    else:
        return "INVALID"

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        identification_number = input()
        print(validate_id_number(identification_number))
