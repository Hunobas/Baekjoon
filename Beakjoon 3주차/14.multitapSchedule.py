import sys
from heapq import heapify, heappop

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    appliances = list(map(int, input().split()))

    cnt = 0
    multitap = []

    for i in range(len(appliances)):
        if appliances[i] in multitap:
            continue

        if len(multitap) == N:

            priorities = []
            for eachTap in multitap:
                j = 0

                while j < len(appliances) - i:
                    j += 1
                    if eachTap != appliances[i + j - 1]:
                        continue
                    else:
                        break
                    
                priorities.append((-j, eachTap))

            heapify(priorities)
            multitap.remove(heappop(priorities)[1])
            cnt += 1
            
        multitap.append(appliances[i])

    print(cnt)