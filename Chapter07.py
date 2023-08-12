msg="It is Time"
print(msg.upper()) #원본은 바뀌지 않는다.
print(msg.lower())
print(msg)

print()

tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #가장 처음 나온 T의 인덱스를 반환해줌
print(tmp.count('T')) #대문자 T가 tmp문자열에 몇개 있는지 개수 리턴
print(msg[:2]) #인덱스 2번전까지 처음부터 뽑아냄
print(msg[3:5])

print()

print(len(msg)) #공백문자 포함 문자열의 길이 출력
for i in range(len(msg)):
    #i는 0부터9까지 탐색
    if(msg[i]==' '):
        continue
    print(msg[i], end=' ')
#이때의 i는 문자열의 인덱스
print()

for x in msg:
    if(x==' '):
        continue
    print(x, end=' ')
#이때의 x는 문자열의 문자
print()

#대문자만 출력
for x in msg:
    if(x.isupper()):
        print(x, end=' ')
print()

#소문자만 출력
for x in msg:
    if(x.islower()):
        print(x, end=' ')
print()

#공백제거하고 출력
for x in msg:
    if(x == ' '):
        continue
    print(x, end='')
print()

#띄어쓰기는 빼고 알파벳만 출력
for x in msg:
    if(x.isalpha()):
        print(x, end='')
print()

#아스키넘버 출력
tmp='AZ'
for x in tmp:
    print(ord(x))
print()

#아스키넘버 출력
tmp='az'
for x in tmp:
    print(ord(x))
print()

#아스키 넘버에 대응하는 문자 출력,
tmp = 122
print(chr(tmp))