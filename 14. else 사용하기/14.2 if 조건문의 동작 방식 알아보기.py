# if 조건문의 동작 방식 알아보기
## 조건식이 아닌 값으로 if와 else의 코드를 동작시켜보자
## True와 False를 사용해주세요!

if True:
    print('참')
else :
    print('거짓')


if False:
    print("참")
else:
    print('거짓')


if None:
    print('참')
else :
    print('거짓')


    # 결론은 TRUE는 참이고, FLASE랑 NONE은 거짓이다.! 실제 코드 작성할 때 많이 사용됩니다!

# IF 조건문에 숫자 지정하기

if 0:
    print('참')

else :
    print('거짓')


if 1:
    print('참')
else :
    print('거짓')

        # 결론은 0은 거짓이고, 0이외의 숫자는 참이다.(실수 포함)

# 문자열과 빈 문자열은 어떠할까?

if 'ciera':
    print('참')

else :
    print('거짓')

if '':  # 빈 문자열
    print('참')
else :
    print('거짓')

        # 결론은 문자열은 참이고, 빈문자열은 거짓이다. (공백이 빈문자열은 절대 아니다@)



