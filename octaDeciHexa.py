import sys

def octaToDeci(octa: str) -> int:
    exp = 0
    factor = 8
    deci = 0
    for c in octa[::-1]:
        deci += (factor ** exp) * int(c)
        exp += 1
    
    return deci

def hexaToDeci(hexa: str) -> int:
    exp = 0
    factor = 16
    deci = 0
    for c in hexa[::-1]:
        coef = 0
        if (c in "abcdef"):
            coef = ord(c) - 87
        else:
            coef = int(c)

        deci += (factor ** exp) * coef
        exp += 1
    
    return deci

if __name__ == "__main__":
    input = sys.stdin.readline

    X = input()[:-1]
    result = 0

    if (X.startswith('0x')):
        result = hexaToDeci(X[2:])
    elif (X.startswith('0')):
        result = octaToDeci(X[1:])
    else:
        result = int(X)

    print(result)