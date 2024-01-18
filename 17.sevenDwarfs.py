import sys

def findSevenDwarfs():
    heights = []
    for _ in range(9):
        nthheight = int(sys.stdin.readline())
        if 0 < nthheight <= 100:
            heights.append(nthheight)

    for i in range(9):
        for j in range(i + 1, 9):
            new_heights = [heights[k] for k in range(9) if k != i and k != j]

            if sum(new_heights) == 100:
                for height in sorted(new_heights):
                    print(height)
                return


if __name__ == "__main__":

    findSevenDwarfs()