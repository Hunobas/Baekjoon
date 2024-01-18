import sys

if __name__ == "__main__":
    n = sys.stdin.readline()[:-1]

    if len(n) == 1:
        n += "0"

    if len(n) == 2:
        n_fix = n
        first_n = n[-1]
        second_n = str(int(n[0]) + int(n[1]))[-1]
        n = first_n + second_n
        cycle = 1
        
        while n != n_fix:
            cycle += 1
            first_n = n[-1]
            second_n = str(int(n[0]) + int(n[1]))[-1]
            n = first_n + second_n
            
        print(cycle)