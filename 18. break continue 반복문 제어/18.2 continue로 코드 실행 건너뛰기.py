## 홀수만 출력하는 문제
# for문에 활용하는 continue

for i in range(100):
    if i % 2 == 0 :  #여기까지 짝수 조건이 맞으면 for i~ 조건식으로 올라가고,
        continue     #나머지가 1 3 처럼 홀수가 나오면 아래 코드가 실행된다.
    print(i)


# while에 활용하는 continue

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue   # 나머지수가 0이면 아래 코드를 실행하지 않고 건너띔
    print(i)