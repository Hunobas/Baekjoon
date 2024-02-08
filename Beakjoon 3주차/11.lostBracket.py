import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    in_eval = input()[:-1]

    eval_list = in_eval.split("-")
    for i in range(len(eval_list)):
        eval_list[i] = eval_list[i].lstrip("0")
    in_eval = "-".join(eval_list)
    
    eval_list = in_eval.split("+")
    for i in range(len(eval_list)):
        eval_list[i] = eval_list[i].lstrip("0")
    in_eval = "+".join(eval_list)

    isInBracket = False
    i = 0

    while i < len(in_eval):
        if in_eval[i] == '-' and not isInBracket:
            in_eval = in_eval[:i + 1] + "(" + in_eval[i + 1:]
            isInBracket = True
            i += 1
        elif in_eval[i] == '-' and isInBracket:
            in_eval = in_eval[:i] + ")" + in_eval[i:]
            isInBracket = False
        i += 1

    if isInBracket:
        in_eval += ")"
    
    print(eval(in_eval))