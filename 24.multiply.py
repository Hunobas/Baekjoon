import sys

# def multiply(base: int, exponent: int, diviser: int) -> int:
#     left_expo = exponent // 2
#     right_expo = exponent - left_expo

#     if base > diviser and exponent == 1:
#         return base % diviser
#     if (left_expo * log(base) < log(diviser)) or (right_expo * log(base) < log(diviser)):
#         return (base ** exponent) % diviser
    
#     if left_expo == right_expo:
#         return (multiply(base, left_expo, diviser) ** 2) % diviser
#     else:
#         return (multiply(base, left_expo, diviser) * multiply(base, right_expo, diviser)) % diviser

def power(base:int, exponent:int, moduler: int) -> int:
    result = 1

    while exponent:
        if exponent % 2 == 1:
            result *= base

        base *= base
        base = base % moduler
        exponent = exponent // 2

    return result

if __name__ == "__main__":
    A, B, C = list(map(int, sys.stdin.readline().split()))

    print(power(A, B, C) % C)