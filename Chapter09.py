# a=[0]*3
# print(a)

a=[[0]*3 for _ in range(3)]
print(a)

a[0][1] = 1
print(a)

a[1][1] = 2
print(a)

print()

for x in a :
    print(x)
print()

for x in a:
    #x가 하나하나 1차원 리스트
    for y in x:
        print(y, end=' ')
    print()
print()