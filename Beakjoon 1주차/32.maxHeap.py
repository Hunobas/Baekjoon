import sys
import heapq

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    xlist = []

    if 1 <= N <= 100000:

        for _ in range(N):
            x = int(sys.stdin.readline())

            if 0 < x < 2 ** 31:
                heapq.heappush(xlist, MaxHeapObj(x))
            elif x == 0:
                try:
                    print(heapq.heappop(xlist).val)
                except IndexError:
                    print(0)
        