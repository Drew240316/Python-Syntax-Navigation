# while 반복문

#x = 0 #초기식

#while x < 30: # 초기식을 보고, 조건식에 따름
    #print("안녕") # 반복할 코드의 내용 작성
    #i += 1      #변화식을 작성

# 조건식부터 ~ 변화식 까지 roof 형태이다.


# 홀수 출력하기
a = 1

while a <= 20:
    print("Hello ! ahahaha ! ", a )
    a += 2 #1부터 시작해서 홀수가 출력! > 짝수는 0으로 초깃값 입력

# 숫자 줄이기

i = 100

while i >0:  # i가 0보다 작을 때 반복해라
    print("TEST! ", i)
    i += -1

# 입력한 횟수대로 반복하기

count = int(input("숫자 입력해주세요:"))

i = 0
while i < count:  # i라는 변수가 count보다 작을 때까지!
    print("Hello world", i)
    i += 1
