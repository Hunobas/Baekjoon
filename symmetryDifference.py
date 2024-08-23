if __name__ == "__main__":
    N, M = list(input().split())
    A = set(list(input().split()))
    B = set(list(input().split()))

    result = len(A) + len(B)

    for a in A:
        if a in B:
            result -= 2

    print(result)
