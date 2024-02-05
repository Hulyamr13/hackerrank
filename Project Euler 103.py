MOD = 715827881

def main():
    N = int(input().strip())

    next_terms = [1, 1]
    sum_terms = [0, 1, 2]

    for i in range(1, N - 1):
        if i % 2 == 1:
            next_terms.append((next_terms[-1] * 2) % MOD)
            sum_terms.append(sum_terms[-1] + next_terms[-1])
        else:
            next_terms.append((sum_terms[-1] - sum_terms[i - (i // 2)]) % MOD)
            sum_terms.append(sum_terms[-1] + next_terms[-1])

    next_terms.reverse()

    prev = 0
    for term in next_terms:
        term = (term + prev) % MOD
        prev = term
        print(term, end=" ")

if __name__ == "__main__":
    main()
