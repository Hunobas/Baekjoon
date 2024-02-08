import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        
        freshmanList = []
        resultList=  []
        
        for _ in range(N):
            A, B = list(map(int, input().split()))
            freshmanList.append((A, B))

        freshmanList.sort()
        resultList.append(freshmanList[0])

        for freshman in freshmanList[1:]:
            if resultList[-1][1] > freshman[1]:
                resultList.append(freshman)

        print(len(resultList))