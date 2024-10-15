# >> 매개변수 초깃값 지정하기
# > 지금까지 함수를 호출할 때, 인수를 넣어서 전달했다.
# > 인수를 생각할 순 없을까? 함수 매개변수에 초깃값 지정하기

# def 함수이름(매개변수=값):
#   코드

# 매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할 때 활용한다.

def personal_info(name, age, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('홍길동',30)
#address를 안적어도 비공개라고 나온다 = 초깃값 설정 완료!

print("'########################'")
personal_info('홍길동', age = 40)

print("'########################'")
# >초깃값 지정 시, 주의사항?
# >매개변수의 초깃값을 지정할 때 한 가지 주의할 점은 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없다
# >address를 두 버 ㄴ재 매개변수로 만들고, 그 다음 초깃값을 지정하지 않은 age가 오도록 만들면, 에러가난다.
# > syntaxerror : non - default argument follows default argumet
#def personal_info(name, address = '비공개', age ):
    #print('이름: ', name)
    #print('나이: ', age)
    #print('주소: ', address)