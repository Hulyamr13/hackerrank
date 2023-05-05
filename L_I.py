from collections import defaultdict


class LetterIslands:

    def __init__(self):
        self.s = 0
        self.k = 0
        self.n = 0
        self.result = 0

    def get_indice(self):
        cache = defaultdict(list)
        for (idx, let) in enumerate(self.s):
            cache[let].append(idx)
        for (key, val) in cache.items():
            l = len(val)
            if l < self.k:
                continue
            else:
                for i in range(len(val) - 1):
                    if val[i + 1] - val[i] <= 1:
                        l -= 1
                if l == self.k:
                    self.result += 1
        return cache

    def get_result(self):
        for (let, pos) in self.get_indice().items():
            len_ = 1
            arr = [[let, pos]]
            while len(arr) > 0:
                dict_ = defaultdict(list)
                temp = []
                for t in arr:
                    for indice in t[1]:
                        try:
                            dict_[t[0] + self.s[indice + len_]].append(indice)
                        except:
                            pass
                len_ = len_ + 1
                for (key, val) in dict_.items():
                    l = len(val)
                    if l < self.k:
                        continue
                    else:
                        i = 0
                        lenVal = len(val)
                        while l >= self.k and i < lenVal - 1:
                            if val[i + 1] - val[i] <= len_:
                                l -= 1
                            i += 1
                        if l == self.k:
                            self.result += 1
                        if l >= self.k - 1:
                            temp.append([key, val])
                arr = temp

        return (self.result)

    def debug(self):
        try:
            self.solve()
            print(self.result)
        except:
            pass

    def solve(self):
        self._input()
        self.get_result()

    def _input(self):
        self.s = input()
        self.k = int(input())
        self.n = len(self.s)


if __name__ == "__main__":
    LetterIslands().debug()
