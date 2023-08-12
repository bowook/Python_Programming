#Chapter03_01 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉽다"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉽다."""
print(sentence3)
print("-------------------------------------")
#Chapter03_02 슬라이싱
#필요한것만큼만 잘라서 사용하는 것
jumin = "000316-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[0:2]) #0~2 미만까지 슬라이싱
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) #처음부터 6직전까지 슬라이싱
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : "  + jumin[7:]) #7부터 끝까지 슬라이싱
print("뒤 7자리 (뒤에서 부터) : " + jumin[-7:]) 
print("-------------------------------------")

#Chapter03_03 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) #소문자 만들기
print(python.upper()) #대문자 만들기
print(python[0].isupper()) #대문자인지 확인
print(len(python)) #문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n") #가장 처음에 만난 n의 인덱스를 return
print(index)

index = python.index("n", index + 1)
#앞에서 만난 n 다음위치부터 탐색하는 방식
print(index)

print(python.find("n")) #가장 처음에 만난 n의 인덱스를 return
print(python.find("Java")) #없는 값일 경우 -1 반환
#print(python.index("Java")) #index에서는 값이 없을 경우 오류 발생, 따라서 프로그램 종료

print(python.count("n")) #n이 총 몇번 등장하는지 파악

#Chapter03_04 문자열 포멧 함수

# print("a" + "b")
# print("a", "b")

print("나는 %d살입니다." %20) #d는 정수를 의미
print("나는 %s을 좋아해요." %"파이썬") #%s는 문자열을 의미
print("Apple 은 %c로 시작해요." %"A") #%c는 문자를 의미

print("나는 %s살입니다."%20)
print("나는 %s색과 %s색을 좋아한다." %("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아한다.".format(age=20, color ="빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아한다.")

#Chapter03_05 탈출 문자
print("백문이 불여일견 \n백견이 불여일타") #\n 줄바꿈

print("저는 \"나도코딩\"입니다.")

print("C:\\Users\\User\\Desktop\\python_basic>")

print("Red Apple\rPine") #\r : 커서를 맨 앞으로 이동

print("Redd\bApple") #\b : 백스페이스 (한글자 삭제)

print("Red\tApple") #\t : Tab