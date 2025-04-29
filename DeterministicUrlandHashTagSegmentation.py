import re


def split_words(line, tokens, regexps):
    #print('line', line, 'tokens', tokens)
    if not line:
        return tokens
    else:
        for regexp in regexps:
            m = regexp.match(line)
            if m:
                matched = m.group(0)
                suffix = line[len(matched):]
                new_tokens = tokens + [matched]
                ans = split_words(suffix, new_tokens, regexps)
                if ans:
                    return ans
        return None


def main():
    with open('words.txt') as f:
        regexps = [re.compile(r'\d+(?:\.\d+)?')]
        for w in sorted(re.split(r'[\n ]+', f.read()), key=len, reverse=True):
            if w:
                regexps.append(re.compile(w, flags=re.IGNORECASE))

        test_num = int(input())
        for n in range(test_num):
            raw_data = input()
            line = ''
            if raw_data[0] == '#':
                line = raw_data[1:]
            else:
                m = re.findall(r'(?:www\.)?(\w+?)\..*', raw_data)
                if m:
                    line = m[0]
            ans = split_words(line, [], regexps)
            if ans:
                print(' '.join(ans))
            else:
                print(raw_data)


if __name__ == '__main__':
    main()
