#람다 함수

# def plus_one(x):
#     return x+1

# print(plus_one(2))

# plus_two=lambda x: x+2
# print(plus_two(1))

#람다함수는 내장 함수의 인자로 사용할 때 편함

def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))

print(list(map(lambda x: x+1, a)))