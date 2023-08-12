#Chapter04_01 리스트

#순서를 가지는 객체의 집합
#비슷한 것들을 하나로 묶어줌
subway = [10, 20, 30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하") #append는 맨뒤에 추가
print(subway)

subway.insert(1,"정형돈") #insert는 원하는 index에 추가
print(subway)

print(subway.pop()) #맨뒤에있는얘 꺼내기
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석")) #같은 객체가 몇개인지 개수 리턴

print("-------------------------------------")

num_list = [5,2,4,3,1]
num_list.sort() #정렬
print(num_list) 
num_list.reverse()
print(num_list)
print("-------------------------------------")

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)
print("-------------------------------------")
#리스트 확장

num_list.extend(mix_list)
print(num_list)

print("-------------------------------------")

#Chapter04_02 사전
#Key : Value 형태
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#get으로 값을 가져올 때 Key가 없는 경우 None이 출력되고 이어나가고
#[]로 Key를 통해 Value에 접근을 할 때 없는 Key면 오류가 나타나고 출력이 이어나가지 않음

print(3 in cabinet)
print(5 in cabinet)

cabinet[5] = "민보욱"
print(5 in cabinet)

print(cabinet)
print("-------------------------------------")
del cabinet[3]
print(cabinet)
print("-------------------------------------")
#Key들만 출력
print(cabinet.keys())
print("-------------------------------------")
#Value들만 출력
print(cabinet.values())
print("-------------------------------------")
#Key:Value 쌍들을 출력
print(cabinet.items())
print("-------------------------------------")
#cabinet 정리
cabinet.clear()
print(cabinet)
print("-------------------------------------")

#Chapter04_03 튜플
#내용 변경 및 추가 못함
#속도가 리스트보다 빨름
#변경되지 않는 목록을 활용할 때 튜플 사용

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#Chapter04_04 세트(set) (집합)
#중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) #1,2,3만 출력됨, => 중복 안됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java 와 python을 모두 할 수 있는 개발자)

print(java & python)
print(java.intersection(python))

print("-------------------------------------")
#합집합 (java 또는 python을 할 수 있는 개발자)

print(java | python)
print(java.union(python))

print("-------------------------------------")
#차집합 (java를 할 줄 알지만 python을 못함)
print(java - python)
print(java.difference(python))

print("-------------------------------------")

#교육을 받아서 python을 할 줄 아는사람이 늘어남
python.add("김태호")
print(python)

print("-------------------------------------")
#java를 까먹었음
java.remove("김태호")
print(java)

print("-------------------------------------")

#Chapter04_06 자료구조의 변경
drinks = {"커피", "우유", "주스"}
print(drinks, type(drinks)) #현재는 집합(set)

drinks = list(drinks) #자료구조 변환
print(drinks, type(drinks))

drinks = tuple(drinks)
print(drinks, type(drinks))

drinks = set(drinks)
print(drinks, type(drinks))