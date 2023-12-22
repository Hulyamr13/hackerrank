def check_hackerrank_position(sentence):
    words = sentence.split()
    if len(words) == 1 and words[0] == 'hackerrank':
        return 0

    if words[0] == 'hackerrank':
        return 1

    if words[-1] == 'hackerrank':
        return 2

    return -1


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        conversation = input()
        result = check_hackerrank_position(conversation)
        print(result)
