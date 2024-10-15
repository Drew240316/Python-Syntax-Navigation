# break는 while for 문에 사용이 가능하다.

i = 0
while True: #조건문
    print(i) #조건문에 따른 수행할 로직
    i += 1 #변화할 식
    if i == 100:
        break #irk 100이면 반복문을 끝내라.while의 제어흐름을 벗어나라


a = 0

for a in range(30):
    print("for문 결과: ", a)
    if a == 22:
        break