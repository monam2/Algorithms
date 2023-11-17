#swea 9280 진용이네 주차타워

T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split())
    fee = []
    for i in range(n):
        fee.append(int(input()))
    weight = []
    for i in range(m):
        weight.append(int(input()))
    grid = [0]*(n+1)
    answer = 0
    wait = []

    for i in range(m*2):
        car = int(input()) #차량 번호
        if car > 0: #차량 들어옴
            if 0 not in grid: #주차장 빈칸 없으면
                wait.append(car)
            else:
                can_park = grid.index(0)
                grid[can_park] = car
                answer += fee[can_park] * weight[car-1]
        else: #차량 나감
            car = car*(-1)
            can_park = grid.index(car)
            if wait: #차량 나갈때 대기줄이 있으면 바로 넣음
                tmp = wait.pop(0)
                grid[can_park] = tmp
                answer += fee[can_park] * weight[car-1]
            else: #그냥 나감
                grid[can_park] = 0

        #         if grid[i] == 0: #주차장 앞에서부터 빈칸이 있음
        #             if wait:
        #                 wait.append(car)
        #                 while wait: #대기줄이 있으면 대기 손님을 넣고, 현재 손님은 대기줄로 이동
        #                     tmp = wait.pop(0)
        #                     grid[i] = tmp
        #                 break
        #             grid[i] = car #대기줄이 없으면 그냥 앞에서부터 빈자리에 현재 손님 넣기
        #             break

        # else: #차량 나감, 만약 대기줄에 손님 있으면 나간 자리에 넣어줘야 함.
        #     car = car*(-1)
        #     for i in grid:
        #         if grid[i] == car:
        #             grid[i] = 0
        #             answer += int(i) * weight[car-1]
        #             break
            
        #     if wait: #차량이 나간 후, 대기 손님이 있으면
        #         for i in grid:
        #             if grid[i] == 0:
        #                 tmp = wait.pop(0)
        #                 grid[i] = tmp
        #                 break
    print(f"#{t} {answer}")

