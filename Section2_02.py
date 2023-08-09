#N개의 숫자로 이루어진 숫자열이 주어지면
#해당 숫자열중에서 s번째부터 e번째 까지의 수를
#오름 차순 정렬했을 때 k번째로 나타나는 수를 출력

testCase = int(input())
#만약 testCase가 2야
#그러면 첫번째 케이스 일때
num_list = []
for i in range(testCase):
    n, s, e, k = map(int, input().split())
    #n은 입력받을 숫자의 개수
    #s번부터 e번까지 오름차순 정렬
    #k번째로 나타나는 수 출력
    num_list = list(map(int,input().split()))
    num_list = sorted(num_list[s-1:e])
    print(num_list[k-1])

#방금 발생한 문제는
#내가 list를 int로 만들었지만
#input을 int로 받아주지 않아서 발생한 문제
#따라서, input을 int로 받아줬으면 바로 해결 가능
#input은 기본적으로 String으로 입력을 받음 => int로 변환



    


    
