import sys
input = sys.stdin.readline
N,S = map(int,input().split())
lst = list(map(int,input().split()))
# N = 5
# S = 0
# lst = [-7, -3, -2, 5,99,99]
cnt = 0

def make(index, current_sum):
    global cnt
    # 선택하지 않은 경우도 고려하기 때문에, index가 N일 경우만 생각해도 
    # 모든 경우의 수가 나옴 
    if index == N:
        if current_sum == S:
            cnt += 1
    else:
        # 현재 원소를 선택하지 않는 경우
        make(index + 1, current_sum)

        # 현재 원소를 선택하는 경우
        make(index + 1, current_sum + lst[index])

# 부분수열을 생성하고 make 함수 호출
make(0, 0)
print(cnt-1 if S == 0 else cnt)