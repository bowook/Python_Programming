a, b = map(int, input().split(' '))

#첫째 줄에 a의 약수들 중 b번째로 작은 수를 출력
#만일 a의 약수의 개수가 b개보다 적으면 -1 출력

count : int = 0
for i in range(1, a+1):
    if(a % i == 0):
        count +=1
    if(count == b):
        print(i)
        break

else:
    print(-1)
        