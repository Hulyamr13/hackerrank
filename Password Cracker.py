import sys

sys.setrecursionlimit(5000)


def solve(attempt, passwords, output, strLoc, memo):
    if strLoc not in memo and strLoc != len(attempt):
        fail_path = True
        for password in passwords:
            if len(password) <= (len(attempt) - strLoc):
                if password == (attempt[strLoc:(strLoc + len(password))]):
                    output.append(password)
                    output = solve(attempt, passwords, output, strLoc + len(password), memo)
                    if len("".join(output)) == len(attempt):
                        fail_path = False
                        break
        if fail_path:
            memo.add(strLoc)

    if strLoc in memo:
        output = output[:-1]

    return output


def main():
    testcases = int(input())
    for i in range(testcases):
        memo = set()
        input()
        passwords = input().split(" ")
        attempt = input()
        output = solve(attempt, passwords, [], 0, memo)
        if len("".join(output)) != len(attempt):
            print("WRONG PASSWORD")
        else:
            print(" ".join(output))


if __name__ == "__main__":
    main()
