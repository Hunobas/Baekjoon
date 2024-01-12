import sys

def ASCIICode(a: str) -> None:
    if (len(a) != 1):
        return
    
    print(ord(a))


if __name__ == "__main__":
    a = sys.stdin.readline()

    ASCIICode(a[:len(a) - 1])