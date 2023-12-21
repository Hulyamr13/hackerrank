import re

TAG_PATTERN = re.compile(r'<\s*(\w+)[^<>]*>')
ATTRIBUTE_PATTERN = re.compile(r'(\w+)\s*=(".*?"|\'.*?\')')

def read_html(N):
    html = ''
    for _ in range(N):
        html += input()
    return html

def main():
    N = int(input())
    html = read_html(N)

    tag2attributes = {}

    tag_matches = re.finditer(TAG_PATTERN, html)
    for match in tag_matches:
        tag = match.group()
        tag_name = match.group(1)

        if tag_name not in tag2attributes:
            tag2attributes[tag_name] = set()

        attribute_matches = re.finditer(ATTRIBUTE_PATTERN, tag)
        for attr_match in attribute_matches:
            attribute_name = attr_match.group(1)
            tag2attributes[tag_name].add(attribute_name)

    for tag_name in sorted(tag2attributes.keys()):
        attributes = ','.join(sorted(tag2attributes[tag_name]))
        print(f"{tag_name}:{attributes}")

if __name__ == "__main__":
    main()
