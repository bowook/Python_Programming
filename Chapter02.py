#Chapter02_01 연산자

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2
print("-------------------------------------")
print(2**3) #8 , 2의 3승
print(5%3) #2 , 나머지 연산자
print(5//3) #1 , 몫 연산자
print(10//3) #3, 몫 연산자
print("-------------------------------------")
print(10>3) #True
print(4 >= 7) #False
print(3 == 3) #True
print(4 == 2) #False
print(3+4 == 7) #True , 연산자 우선순위가 더하기가 더 높음.
print(1 != 3) #True
print(not(1 != 3)) #False
print("-------------------------------------")
print((3>0) and (3<5)) #True, and 연산자는 두 항이 모두 True여야 True
print((3>0) & (3<5)) #True
print((3<0) and (3<5))
print("-------------------------------------")
print((3>0) or (3>5)) #True,, or 연산자는 두 항중 하나만 True여도 True

print(5>4>3) #True
print(5>4>7) #False
print("-------------------------------------")


#Chapter02_02 수식
print(2+3*4) #14
print((2+3)*4) #20
number = 2 + 3 * 4 #14
print(number) #14
number = number + 2 #16
print(number) #16
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1
print(number)
print("-------------------------------------")

#Chapter02_03 숫자 처리
print(abs(-5)) #5 , 절대값 반환
print(pow(4,2)) #16, 4의 2승
print(max(5,12)) #12, 최대값 찾기
print(min(5,12)) #5, 최소값 찾기
print(round(3.14)) #3, 반올림
print(round(4.99)) #5, 반올림

from math import * #math 라이브러리를 이용
print(floor(4.99)) #4, #내림
print(ceil(3.14)) #4, 올림
print(sqrt(16)) #4, 제곱근
print("-------------------------------------")

#Chapter02_04 랜덤 함수
from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의의 값 생성
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성

#로또값 출력 1~45 이하의 임의의 값 생성
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
