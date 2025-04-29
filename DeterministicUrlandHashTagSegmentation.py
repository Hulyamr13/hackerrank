import re


def split_words(line, tokens, regexps):
    if not line:
        return tokens

    for regexp in regexps:
        match = regexp.match(line)
        if match:
            matched = match.group(0)
            suffix = line[len(matched):]
            new_tokens = tokens + [matched]
            result = split_words(suffix, new_tokens, regexps)
            if result:
                return result
    return None


def load_regexps_from_file(filename):
    with open(filename, encoding='utf-8') as f:
        words = re.split(r'[\n\s]+', f.read())
        sorted_words = sorted(filter(None, words), key=len, reverse=True)

    regexps = [re.compile(r'\d+(?:\.\d+)?')]
    regexps.extend(re.compile(re.escape(w), flags=re.IGNORECASE) for w in sorted_words)
    return regexps


def extract_line(raw_data):
    if raw_data.startswith('#'):
        return raw_data[1:]
    match = re.search(r'(?:www\.)?(\w+)\.', raw_data)
    return match.group(1) if match else ''


def main():
    regexps = load_regexps_from_file('words.txt')

    try:
        test_num = int(input())
    except ValueError:
        return

    for _ in range(test_num):
        raw_data = input().strip()
        line = extract_line(raw_data)
        if not line:
            print(raw_data)
            continue

        result = split_words(line, [], regexps)
        if result:
            print(' '.join(result))
        else:
            print(raw_data)


if __name__ == '__main__':
    main()

