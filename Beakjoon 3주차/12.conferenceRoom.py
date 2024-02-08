import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    conferList = []

    for _ in range(N):
        start, end = list(map(int, input().split()))
        conferList.append((end, start))

    conferList.sort()
    resultList = []
    resultList.append(conferList[0])
    
    for confer in conferList[1:]:
        # 다음 회의 시작 시각 >= 이번 회의 끝나는 시각
        if confer[1] >= resultList[-1][0]:
            resultList.append(confer)
    
    print(len(resultList))