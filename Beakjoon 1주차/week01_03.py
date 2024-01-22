import sys

input= sys.stdin.readline

# N = 8
# lst = ['11110000',
#         '11110000',
#         '00011100',
#         '00011100',
#         '11110000',
#         '11110000',
#         '11110011',
#         '11110011']

N = int(input())
lst = []

for i in range(N):
    lst.append(input().replace('\n',''))

lst = [list(map(int, char)) for char in lst]

def devide(lst) :
    result = sum(sum(row) for row in lst)
    if result == 0 :
        print(0,end='')
    elif result == len(lst)*len(lst) :
        print(1,end='')
    else :
        mid = len(lst) //2 
        print('(',end='')
        devide([row[:mid] for row in lst[:mid]])
        devide([row[mid:] for row in lst[:mid]])
        devide([row[:mid] for row in lst[mid:]])
        devide([row[mid:] for row in lst[mid:]])
        print(')',end='')

devide(lst)