import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    LessonLengths = list(map(int, input().split()))

    MeanLength = sum(LessonLengths) // M

    LengthAccumulate = 0
    VideoGroup = []

    for i in range(N):
        LengthAccumulate += LessonLengths[i]
        if i == N - 1 and len(VideoGroup) == M - 1:
            VideoGroup.append(LengthAccumulate)
        elif i == N - 1:
            VideoGroup.append(LengthAccumulate - LessonLengths[i])
            VideoGroup.append(LessonLengths[i])
        elif LengthAccumulate > MeanLength and i == 0:
            VideoGroup.append(LessonLengths[i])
            LengthAccumulate = 0
        elif LengthAccumulate > MeanLength:
            VideoGroup.append(LengthAccumulate - LessonLengths[i])
            LengthAccumulate = LessonLengths[i]

    print(max(VideoGroup))
