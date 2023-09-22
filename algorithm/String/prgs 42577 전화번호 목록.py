#프로그래머스 전화번호 목록
def solution(phone_book):
    dic = {}

    for i in phone_book:
        dic[i] = True
    for number in phone_book: #number : 119
        temp = ""
        for n in number: # n : '1'
            temp += n
            if temp in dic and temp != number:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["117","1178","119","123","13"]))
