#현수는 N장의 카드를 가지고 있음.
#같은 숫자 여러장 가능 (중복 허용)
#이중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록
#3장을 뽑을 수 있는 모든 경우를 기록
#기록한 값중 K번째로 큰 수 출력
import random as r
card_count,max_num = map(int, input().split())
card_number = list(map(int, input().split()))
# delete_number = list(set(card_number))
# delete_number.sort(reverse=True)
# print(delete_number[max_num-1])
choice_temp : int = 0
choice_sum : int = 0
choice_arr = []

for i in range(1,len(card_number)):
    choice_temp=r.choice(card_number)
    print(choice_temp)
    if(choice_temp in card_number):
        choice_sum += choice_temp
        if(i % 3 == 0):
            choice_arr.append(choice_sum)
            print(choice_arr)
            choice_sum = 0
        card_number.pop(card_number.index(choice_temp))
        print(card_number)

choice_arr.sort(reverse=True)
print(choice_arr[max_num-1])




