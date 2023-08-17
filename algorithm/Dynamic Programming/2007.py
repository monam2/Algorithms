#패턴 마디의 길이
T = int(input())
for test_case in range(1, T + 1):
    s = input()
    start = s[0]
    for i in range(1,len(s)):
        result = ''
         
        if s[i] == start:
            new_s = s.replace(s[:i], '')
            if new_s == ''or len(new_s) < len(s[:i]):
                result = s[:i]
                break
    print(f'#{test_case}', len(result))
