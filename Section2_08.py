#뒤집은 소수

#N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면
#그 수를 출력하는 프로그램
def reverse(x):
    temp_number = []
    for i in range(0, len(x)):
        temp_number.append(x[i][::-1])
        
    result = []
    for i in range(0, len(temp_number)):
        count = 0
        for j in str(temp_number[i]):
            if j == '0':
                count += 1
            else:
                break
        result.append(str(temp_number[i])[count:])

    return isPrime(result)

def isPrime(x):
    prime_list = []
    for i in range(0, len(x)):
        count : int = 0
        for j in range(2, int(x[i])):
            if(int(x[i]) % j == 0):
                count += 1
                break
        if(count == 0):
            prime_list.append(x[i])
    return prime_list

num_count = int(input())
num_list = list(map(str, input().split()))
real_prime = reverse(num_list)

for i in range(0, len(real_prime)):
    print(real_prime[i] , end =' ')
