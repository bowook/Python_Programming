#Chapter01_01 숫자 자료형

print(5)
print(-10)
print(3.14)
print(5*(2+3))

print("-------------------------------------")

#Chapter01_02 문자열 자료형
print('풍선') #작은 따옴표
print("나비") #큰 따옴표
print("ㅋ"*9) #문자열과 정수를 섞어서 출력 가능
print("-------------------------------------")


#Chapter01_03 Boolean 참/거짓
print(5 > 10)
print(5 < 10) 
print(not True)
print(not (5>10))
print("-------------------------------------")


#Chapter01_04 변수

#애완동물을 소개해 주세요~

#변수는 값을 저장하는 공간
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age>=3

print("우리집" + animal + "의 이름은"+name)
#print(name+"이는 "+ str(age) +"살이며, 산책을 아주 좋아함")
print(name,"이는 ", age ,"살이며, 산책을 아주 좋아함")
name = "이름변경"

#정수형을 출력할 때는 str로 바꿔줘야함.
print(name+"이는 어른일까요?"+ str(is_adult))
#Boolean을 출력할 때도 str로 바꿔줘야함.
print("-------------------------------------")

#Chapter01_05 주석 처리
'''이렇게 하면
여러 문장 주석 처리 가능'''

# 또는 주석처리 하고싶은것을 드래그 한 후 , Ctrl  + / 누르면
# 전체 슬래시

# 취소를 원할 때도 Ctrl + /