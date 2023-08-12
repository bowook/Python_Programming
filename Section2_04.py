import math as math
n = int(input())
a = list(map(int, input().split()))
ave = math.ceil(sum(a)/n)
#round는 round_half_even 방식을 택함.
min = 2147000000

#idx는 학생 번호
#x는 학생 성적
#enumerate는 인덱스값과 실제 값을 쌍으로 대응해주는 함수
for idx, x in enumerate(a):
    tmp=abs(x-ave) #이렇게 해야 평균과 가까운 값을 찾을 수 있음
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(ave, res)







