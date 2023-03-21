from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        if attrs:
            print("Empty :", tag)
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
        else:
            print("Empty :", tag)


parser = MyHTMLParser()
parser.feed(''.join(input() for _ in range(int(input()))))
