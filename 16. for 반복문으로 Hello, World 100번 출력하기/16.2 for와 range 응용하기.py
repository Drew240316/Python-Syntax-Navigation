# 시작하는 숫자와 끝나는 숫자 범위 지정하기

for i in range(5,12):
    print("Hello World",i)


for i in range(0,20,2): #증가폭 사용
    print("Hello Simson",i)


# 숫자를 감소시킬 수 있을까? - 증가폭 사용

for i in range(10,0,-2):
    print("Hello marji", i)

# 증가폭만 사용해서 바꾸는건가? 아니다! reversed()함수 사용 가능하다!

for i in reversed(range(10)):
    print("Hello margi!!",i)

# 입력한 횟수대로 반복할 수 있을까?

count = int(input())

for i in range(count):
    print("count", i)