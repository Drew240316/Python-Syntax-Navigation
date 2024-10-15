# FOR문을 사용한 홀수 출력:
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


#  while True를 사용한 홀수 출력:
i = 1
while True:
    if i % 2 != 0:
        print(i)
    i += 1
    if i > 10:
        break

# 범위를 논리 연산자로 지정한 while문 홀수 출력:

i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


