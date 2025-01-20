# 1337 올바른 배열

def search_func(N, numbers):
    numbers.sort()

    min_value = float('inf')

    for i in range(N):
        j = i

        while j < N and numbers[j] - numbers[i] < 5:
            j += 1
        
        min_value = min(min_value, 5 - (j-i))

    return min_value

N = int(input())
arr = [int(input()) for _ in range(N)]

print(search_func(N, arr))