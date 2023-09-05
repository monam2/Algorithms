#프로그래머스 12981

def solution(n, words):
    result = []
    end = words[0][0]
    for i, value in enumerate(words):
        if end != words[i][0] or words[i] in result:
            return [i%n+1, i//n+1]
        result.append(value)
        end = value[-1]
    return [0,0]
            
        

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution(4, ["hello", "one", "even", "even", "now", "draw"]))
