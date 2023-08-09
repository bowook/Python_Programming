#정다면체
#두 개의 정 N,M면체의 주사위를 던져서 나올 수 있는 눈의 합
#중에서 가장 확률이 높은 숫자를 출력
#여러개일경우 오름차순으로 출력

#첫 번째 줄에는 자연수 N,M 주어짐, N,M은 4,6,8,12,20중 하나

N,M = map(int, input().split())
sum_count = []
count : int = 0
index = []
high_percent = []
for i in range(1,N+1):
    #만약 N이 4가 나왔다라고 했을 때, i가 1
    for j in range(1, M+1):
        #그러면 j도 1부터 M까지 다 더해서 리스트에 추가
        sum_count.append(i+j)

print(sum_count)
for i in range(0,len(sum_count)):
    count = sum_count.count(sum_count[i])
    index.append(count)

for i in range(0, len(index)):
    if(index[i] < max(index)):
        continue
    elif(index[i] == max(index)):
        if(sum_count[i] in high_percent) :
            continue
        else :
            high_percent.append(sum_count[i])

high_percent.sort()

print(high_percent)
