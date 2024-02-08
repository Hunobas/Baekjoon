import sys
input = sys.stdin.readline

n = int(input())

stair = [0] * 301
for i in range(1, n+1):
    stair[i] =int(input())

d = [0]*301
d[1] =stair[1]
d[2] =stair[1]+stair[2]
# d[3] =max(stair[1] + stair[3], stair[2]+stair[3])

for i in range(3, n+1):
    d[i] =max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])

print(d[n])