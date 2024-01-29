def main():
    while True:
        try:
            n, q = map(int, input().split())
            mp = [{} for _ in range(8)]
            ans = n * (n + 1) // 2
            s = input().strip()
            for i in range(n):
                t = 0
                for j in range(8):
                    if j + i < len(s):
                        t = t * 26 + ord(s[i + j]) - ord('a')
                        if t not in mp[j]:
                            mp[j][t] = 1
                        else:
                            ans -= 1
                            mp[j][t] += 1

            for _ in range(q):
                k, c = input().split()
                k = int(k) - 1
                for i in range(max(0, k - 7), k + 1):
                    t = 0
                    for j in range(8):
                        if j + i < len(s):
                            t = t * 26 + ord(s[i + j]) - ord('a')
                            if i + j < k:
                                continue
                            mp[j][t] -= 1
                            if mp[j][t] == 0:
                                del mp[j][t]
                                ans -= 1

                s = s[:k] + c + s[k + 1:]

                for i in range(max(0, k - 7), k + 1):
                    t = 0
                    for j in range(8):
                        if j + i < len(s):
                            t = t * 26 + ord(s[i + j]) - ord('a')
                            if i + j < k:
                                continue
                            if t not in mp[j]:
                                mp[j][t] = 1
                                ans += 1
                            else:
                                if mp[j][t] == 0:
                                    ans += 1
                                mp[j][t] += 1

                print(ans)

        except EOFError:
            break

if __name__ == "__main__":
    main()
