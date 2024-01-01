from string import ascii_uppercase as alphabet

def decode(keyword, message):
    unique_keyword = ''.join([char for i, char in enumerate(keyword) if keyword.index(char) == i])

    remaining_alphabet = ''.join([char for char in alphabet if char not in unique_keyword])

    ordered_chars = unique_keyword + remaining_alphabet

    columns = sorted([''.join([ordered_chars[i] for i in range(n, len(ordered_chars), len(unique_keyword))])
                      for n in range(len(unique_keyword))])

    decoding_dict = {char: replacement for replacement, column_chars in zip(alphabet, ''.join(columns))
                     for char in column_chars}

    decoded_message = ''.join(decoding_dict[char] if char in decoding_dict else ' ' for char in message)
    return decoded_message

test_cases = int(input())

for _ in range(test_cases):
    keyword = input()
    message = input()
    result = decode(keyword, message)
    print(result)
