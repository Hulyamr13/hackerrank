import os


def missingCharacters(s):
    l = [0] * 123
    result = ""
    i = 0
    while i < len(s):
        x = ord(s[i])
        l[x] += 1
        i += 1
    j = 48
    while j <= 57:
        if l[j] == 0:
            result += chr(j)
        j += 1
    k = 97
    while k <= 122:
        if l[k] == 0:
            result += chr(k)
        k += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
