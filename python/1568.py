# 1568 새
def count_seconds_to_fly_away(N):
    time = 0
    k = 1

    while N > 0:
        if N < k:
            k = 1
        N -= k
        k += 1
        time += 1

    return time


N = int(input())
print(count_seconds_to_fly_away(N))
