#Chapter05_01 조건(if)

# weather = input("오늘 날씨는 어때요? ")
# # if 조건: 
# #     실행 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# x = 12
# if x>=10:
#     if x%2==1:
#         print("10이상의 홀수")
# x = 7
# if x>0 and x<10:
#     print("10보다 작은 자연수")
# x = 7
# if 0<x<10:
#     print("10보다 작은 자연수")

#Chapter05_02 반복문(For)

# a = range(1, 11)
# print(list(a))

# for i in range(1, 11):
#     print(i)

# for i in range(10,0, -2):
#     print(i)

#Chapter05_03 반복문(While)
# i = 10
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while True:
#     print(i)
#     if i==5:
#         break
#     i+=1

# for i in range(1,11):
#     if(i%2==0):
#         continue
#     #밑에 있는 부분을 다 건너뛰고 반복문을 진행하는게 continue
#     print(i)

for i in range(1,11):
    print(i)
    if (i>15):
        break
else:
    print(11)

