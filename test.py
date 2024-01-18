
import sys

list = sys.stdin.readline().split(" ")
if len(list) == 1:
    todo = list[0][:-1]
    print(todo)
elif len(list) == 2:
    push = list[0]
    my_int = int(list[1])
    print(push)
    print(my_int)