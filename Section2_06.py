#N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
#그 합이 최대인 자연수를 출력하는 프로그램
#각 자연수의 자릿수의 합을 구하는 함수를
#자릿수의 합이 최대인 자연수를 출력하고,
#자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력
#def digit_sum(x)를 꼭 작성해서 프로그래밍
N = int(input())
num = []
sum_list = []
def digit_sum(x):
    for i in range(0,len(x)):
        sum = 0
        for j in x[i]:
            sum += int(j)
        sum_list.append(sum)
    index = sum_list.index(max(sum_list))
    return print(num[index])
    # if(sum_list.count(max(sum_list)) == 1):
    #     #그러면 같은 값이 없다란소리임
    #     index = sum_list.index(max(sum_list))
    #     return print(num[index])
    # else :
    #     #같은 값이 있을 때 가장 앞에꺼
    #     #아니 잠만
    #     #같은 값이 있든 말든
    #     #index는 어차피 가장 앞에꺼 해주니까
    #     #같은값이 없으면 알아서 최대의 인덱스를 가져올거고
    #     #그러면 조건문을 해줄 필요가 없네
    #     return print(sum_list)

for i in range(0, N):
    num.append(input())

digit_sum(num)
