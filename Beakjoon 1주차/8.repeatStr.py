import sys

def repeatStr(S: str, R: int) -> None:
    if not (1 <= R <= 8):
        return
    if not (1 <= S <= 20):
        return
    
    P = ""
    for i in S:
        for _ in range(R):
            P += i

    print(P)


if __name__ == "__main__":
    
    T = int(sys.stdin.readline())
    largeSR = []

    ### 문제를 잘 읽을 것
    for _ in range(T):
        SR = sys.stdin.readline().split()
        largeSR.append(SR)
        S = str(SR[1]) if len(SR) == 2 else ""
        R = int(SR[0]) if len(SR) == 2 else 0

        repeatStr(S, R)