n = int(input())
a = []
for i in range(n):
    a.append(input())

class StringAsInt(object):
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        if len(self.obj) != len(other.obj):
            return len(self.obj) < len(other.obj)
        else:
            return self.obj < other.obj
    def __gt__(self, other):
        return other < self
    def __eq__(self, other):
        return self.obj == other.obj
    def __le__(self, other):
        return not (self > other)
    def __ge__(self, other):
        return (other <= self)
    def __ne__(self, other):
        return self.obj != other.obj

a.sort(key = StringAsInt)
for x in a:
    print(x)