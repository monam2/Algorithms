#프로그래머스 12915

def solution(strings, n):
    strings.sort(key=lambda v : (v[n],v))
    
    return strings
