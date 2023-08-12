# 반복문을 이용한 문제풀이

# 1) 1부터 N까지 홀수출력하기
# 2) 1부터 N까지 합 구하기
# 3) N의 약수 출력 하기

N = int(input())

print("---------------------------------")
print("Number01")

for i in range(1, N+1):
    if(i%2==0):
        continue
    print(i)

print("---------------------------------")
print("Number02")

sum = 0
for i in range(1, N+1):
    sum += i
print(sum)

print("---------------------------------")
print("Number03")

for i in range(1, N+1):
    if(N%i!=0):
        continue
    else:
        print(i)