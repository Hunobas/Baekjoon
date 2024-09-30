import sys

def can_record(lectures, max_size, m):
    count = 1
    current_sum = 0
    for lecture in lectures:
        if current_sum + lecture > max_size:
            count += 1
            current_sum = lecture
        else:
            current_sum += lecture
        if count > m:
            return False
    return True


def find_min_size(lectures, m):
    left = max(lectures)
    right = sum(lectures)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_record(lectures, mid, m):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    LessonLengths = list(map(int, input().split()))

    print(find_min_size(LessonLengths, M))
