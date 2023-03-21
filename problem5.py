import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score


if __name__ == '__main__':
    n = int(input())
    xml_str = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml_str))
    root = tree.getroot()
    print(get_attr_number(root))
