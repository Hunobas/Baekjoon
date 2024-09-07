from itertools import combinations


def solution(N, K, words):
    if K < 5:
        return 0
    if K == 26:
        return N

    base = set("antatica")

    word_bits = [0] * N
    for i in range(N):
        for c in words[i]:
            if c not in base:
                if ord(c) < ord("c"):
                    word_bits[i] |= 1 << (ord(c) - 98)
                elif ord(c) < ord("i"):
                    word_bits[i] |= 1 << (ord(c) - 99)
                elif ord(c) < ord("n"):
                    word_bits[i] |= 1 << (ord(c) - 100)
                elif ord(c) < ord("t"):
                    word_bits[i] |= 1 << (ord(c) - 101)
                else:
                    word_bits[i] |= 1 << (ord(c) - 102)

    def count_readable(learned):
        cnt = 0
        for word in word_bits:
            if word & learned == word:
                cnt += 1
        return cnt

    max_readable = 0
    for comb in combinations(range(21), K - 5):
        learned = 0
        for i in comb:
            learned |= 1 << i
        max_readable = max(max_readable, count_readable(learned))

    return max_readable


N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]
print(solution(N, K, words))
