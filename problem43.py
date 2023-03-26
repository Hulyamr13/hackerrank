import re

for _ in range(int(input())):
    uid = input().strip()
    if len(uid) != 10:
        print("Invalid")
    elif not re.match(r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[A-Za-z0-9]{10}$', uid):
        print("Invalid")
    else:
        print("Valid")