class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        self.current += 2
        return self.current - 2


class OddStream:
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    if isinstance(stream, OddStream):
        for i in range(n):
            print(stream.get_next())
    else:
        for i in range(n):
            print(stream.get_next())


if __name__ == '__main__':
    queries = int(input().strip())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == 'odd':
            print_from_stream(n, OddStream())
        else:
            print_from_stream(n)
