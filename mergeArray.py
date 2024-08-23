if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []
    i = j = 0

    while i < N and j < M:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    result.extend(A[i:])
    result.extend(B[j:])

    print(" ".join(map(str, result)))
