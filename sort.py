# 학생들 중 점수 상위 10명을 알아내시오(점수가 같으면 알파벳 순서)

arr = [
  ('John', 20),
  ('Chloe', 50),
  ('Ben', 45),
  ('Diana', 35),
  ('Evan', 55),
  ('Fiona', 25),
  ('George', 60),
  ('Hannah', 40),
  ('Ian', 70),
]

result = sorted(arr, key=lambda x : (x[1], x[0]), reverse=True)
print(result)