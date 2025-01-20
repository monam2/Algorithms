# 14405 피카츄

s = input()

words = ["pi", "ka", "chu"]

for word in words:
    s = s.replace(word, "**")

s = s.replace("*", "")

if s == "":
    print("YES")
else:
    print("NO")
