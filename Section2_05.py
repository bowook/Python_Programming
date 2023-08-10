#정다면체
#두 개의 정 N,M면체의 주사위를 던져서 나올 수 있는 눈의 합
#중에서 가장 확률이 높은 숫자를 출력
#여러개일경우 오름차순으로 출력

#첫 번째 줄에는 자연수 N,M 주어짐, N,M은 4,6,8,12,20중 하나

N, M = map(int, input().split())
count = [0] * (N*M)
#N+M을 해주는 이유는,
#두개의 정다면체의 주사위를 굴려서 나올 수 있는 눈의 합의 경우의 수이다.
#1, 2, 3, 4
#1, 2, 3, 4, 5, 6
# => 2, 3, 4, 5, 6, 7, 8, 9, 10
for i in range(1, N+1):
    for j in range(1, M+1):
        #인덱스가 합, value는 개수
        count[i+j]+=1

count_sort = list(filter(lambda x: count[x] == max(count), range(len(count))))

print(count_sort)