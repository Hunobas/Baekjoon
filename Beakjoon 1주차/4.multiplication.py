import sys

def multiplication(n: int) -> None:
    if not (1 <= n <= 9):
        return
    
    for i in range(9):
        print(f"{n} * {i + 1} = {n * (i + 1)}")


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    multiplication(n)