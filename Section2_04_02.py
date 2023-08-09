#평균에 가장 가까운 학생의 몇 번째인지 1번부터 시작
#평균과 가장 가까운 점수가 여러 개일 경우, 먼저 점수가 높은 학생의 번호로 답
import math as math
std_total_num = int(input())
std_total_score = list(map(int,input().split()))
std_score_avg = math.ceil(sum(std_total_score)/std_total_num)
min = float('inf')
for idx, score in enumerate(std_total_score):
    temp = abs(score - std_score_avg)
    if(temp < min):
        min = temp
        score_temp = score
        std_cur_number = idx+1
    elif(temp == min):
        if(score_temp < score):
            std_cur_number = idx+1
            score_temp = score

print(std_score_avg, std_cur_number, end=' ')

