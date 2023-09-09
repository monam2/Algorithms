#13305 주유소

n = int(input())
dist = list(map(int,input().split()))
price = list(map(int, input().split()))
std_price = 0
total_price = 0

for i in range(n-1):
    if i == 0:
        std_price = price[i]
    else:
        std_price = min(std_price, price[i])
    total_price += std_price * dist[i]
  
print(total_price)
