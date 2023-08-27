#1874 스택 수열

n = int(input())
arr=[] #4 3 6 8 7 5 2 1
for i in range(n):
    arr.append(int(input()))
stack=[]
result_st = []
result=[]
k=0
for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == arr[k]:
        p = stack.pop()
        result_st.append(p)
        result.append('-')
        k += 1

if result_st == arr:
    for i in result:
        print(i)
else:
    print('NO')
