import sys
import xml.etree.ElementTree as etree


def get_max_depth(node, depth):
    max_depth = depth
    for child in node:
        child_depth = get_max_depth(child, depth+1)
        max_depth = max(max_depth, child_depth)
    return max_depth


if __name__ == '__main__':
    n = int(input())
    xml_str = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml_str))
    root = tree.getroot()
    print(get_max_depth(root, 0))
