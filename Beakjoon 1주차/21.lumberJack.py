import sys


if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    wood_heights = list(map(int, sys.stdin.readline().split()))

    if 1 <= N <= 1000000 and 1 <= M <= 2000000000:
        if len(wood_heights) == N:
            fix = max(wood_heights)
            max = 0
            min = fix
            sum_wood = 0

            while fix - min <= fix - max:
                mid = (2 * fix - min - max + 1) // 2
                cut_heights = [wood_height - mid for wood_height in wood_heights if wood_height > mid]
                pre_sumWood = sum_wood
                sum_wood = sum(cut_heights)

                if pre_sumWood == sum_wood:
                    if sum_wood < M:
                        mid -= 1
                    break

                if sum_wood > M:
                    min = fix - mid + N
                elif sum_wood < M:
                    max = fix - mid - N
                else:
                    break

            print(mid)