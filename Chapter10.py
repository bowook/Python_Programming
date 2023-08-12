#def로 함수 정의
#특정 작업을 반복해야 할 때, 함수로 정의
#유지보수가 필요할 때, 그 함수만 수정하면 굳
#메인스크립트 위에다가 작성을 해야함
#그래야 함수를 인식하고 사용 가능

# def add(a, b):
#     c=a+b
#     print(c)

# add(3,2) #함수 호출
# add(5,7)

# def add(a, b):
#     c=a+b
#     return c

# #함수로 3, 2를 값을 전달하고, 함수에서 c를 리턴해서
# #Main Script에서 print를 통해 받은 c를 사용
# #return는 함수가 종료된다는 의미
# x = add(3, 2)
# print(x)

# def addAndMinus(a, b):
#     c=a+b
#     d=a-b
#     return c, d

# x = addAndMinus(3,2)
# print(x)

def isPrime(x):
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

a=[12, 13, 7, 9, 19]

#왜냐면 return값이 Boolean이니까, 조건식에 함수만 호출하는 식을 넣으면됨
for i in a:
    if(isPrime(i)):
        print(i, end=' ')
print()



