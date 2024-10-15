x = int(input())


if x == 10:
    print('x가 10입니다')
elif x == 20:
    print('x가 20입니다')
else :
    print('x는 어디에도 속하지 않습니다.')


x = int(input("11에서 100사이의 마음에 드는 정수를 입력하라.: "))

if 11 < x < 20 :
    print('11~20')
elif 21 < x < 30 :
    print('21~30')
else :
    print('아무것도 해당하지 않음')