#Quiz
#사이트별로 비밀번호를 만들어 주는 프로그램 작성

#EX) http://naver.com
#규칙 1 : http://부분은 제외 => naver.com
#규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

#EX) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"생성된 비밀번호 : {password}" )