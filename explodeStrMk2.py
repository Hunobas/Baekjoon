def solution(string, bomb):
    stack = []
    bomb_length = len(bomb)

    for char in string:
        stack.append(char)
        if len(stack) >= bomb_length and "".join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]

    result = "".join(stack)
    return result if result else "FRULA"


# 입력 받기
string = input().strip()
bomb = input().strip()

# 결과 출력
print(solution(string, bomb))
