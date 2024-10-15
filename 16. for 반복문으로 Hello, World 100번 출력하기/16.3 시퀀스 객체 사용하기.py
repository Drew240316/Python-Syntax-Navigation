# FOR에 RNAGE를 사용하면서 시퀀스 객체를 넣어도된다.(튜플,리스트,문자열 등)
# 리스트의 요소를 꺼내서 반복한다.

# 리스트

list = [1,2,3,4,5]

for i in list:  #range 안썻음 , list의 원소값들을 하나씩 건네주세요

    print(i)


# 튜플
fruits = ('apple','banana','orange')

for i in fruits :
    print(i)


# 문자열
home = 'home'
for i in 'home':
    print(home, end = '_') #원래는 줄을 바꾸고 출력하는데, 옆에 이어서 출력하려면? end = ' '을 사용 가능

# 문자열 home을 뒤집어서 가능할까요?
for i in reversed("home"):
    print(home, end =  '+')

# 리스트에 10을 곱해서 출력해라

x = [1,2,3,4,5]

for i in x:
    print(i * 10)