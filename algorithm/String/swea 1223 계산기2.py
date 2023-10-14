#swea 1223 계산기2

for t in range(10):
    n = int(input())
    arr = list(map(str, input().split('+')))
    new_arr =[]
    ex = []
    for i in arr:
        if i.isdigit():
            new_arr.append(int(i))
        else:
            ex.append(i)
    result = sum(new_arr)

    for i in ex: #5*6
        gop = 1
        a = i.split('*') #['5','6']
        for j in a:
            gop = gop * int(j)
        result+= gop
    print(f"#{t+1}", result)
