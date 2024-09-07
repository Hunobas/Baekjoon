import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    cards = list(map(int, input().split()))

    result = 0

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                sum_cards = cards[i] + cards[j] + cards[k]
                if sum_cards <= M and sum_cards > result:
                    result = sum_cards

    print(result)
