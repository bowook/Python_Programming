import random as r

a=[]
print(a)
b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[:5])
print()

b=list(range(1,11))
print(b)

c=a+b
print(c)
print()

print(a)
a.append(6) #리스트의 제일 뒤에 6추가
print(a)
a.insert(3,7) #리스트의 3번 인덱스에 7이 추가
print(a)
a.pop() #리스트의 맨 뒤에 값을 빼낸다
print(a)
print(a.pop()) #이렇게도 빠지네
print(a)
a.pop(3) #3번 인덱스 빼기
print(a)
print()

a.remove(4) #인덱스가 아닌 값을 제거
print(a)
print()

print(a.index(3)) #3이라는 값의 인덱스 번호를 반환해줌
print()

a=list(range(1,11))
print(a)
print(sum(a)) #a리스트의 값들을 다 합
print(max(a)) #a리스트의 값들중 최대값
print(min(a)) #a리스트의 값들중 최소값

r.shuffle(a) #a라는 리스트를 무작위로 섞기
print(a)
a.sort(reverse=True) #내림차순으로 정렬 reverse를 True
print(a)
a.sort() #기본적으로 오름차순으로 정렬
print(a)
a.clear() #리스트 빈 리스트 만들기
print(a)

a=[23, 12, 36, 53, 19]

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if(x%2==0):
        print(x, end=' ')
print()

#튜플 형태로 출력
for x in enumerate(a):
    print(x)
print()

#튜플은 값을 변경할 수 없고, 리스트는 값을 변경할 수 있다.
b=(1,2,3,4,5)
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

#튜플을 자주 쓰는 방식
for index, value in enumerate(a):
    print(index, value)
print()

#리스트 안에 있는 모든 value들의 조건을 비교하는것
#따라서 모든 조건이 참일 경우 True 반환
#하나라도 거짓일 경우 False 반환
if all(60>x for x in a):
    print("YES")
else:
    print("NO")
print()

#리스트 안에 있는 모든 value들의 조건을 비교하는것
#따라서 한번이라도 참일 경우 True 반환
#모두다 거짓일 경우 False 반환
if any(12>x for x in a):
    print("YES")
else:
    print("NO")
print()

for i in range(2):
    print(i)



