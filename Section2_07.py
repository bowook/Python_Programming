#에라토스테네스 체 ( 소수 )
#자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력
#만약 20이 입력되면 1 ~ 20까지의 소수는 총 8개
#2, 3, 5, 7, 11, 13, 17, 19
import math
def prime(x):
    prime_arr = [True] * (x+1)
    prime_arr[0] = [False]
    prime_arr[1] = [False]
    for i in range(2, int(math.sqrt(x)+1)):
        if prime_arr[i] == True:
            j = 2
            while ( i * j ) <= x:
                prime_arr[i*j] = False
                j += 1
    return print(prime_arr.count(True))

N = int(input())
prime(N)
