def mul(a,b):  #순서6.mul함수를 찾음
    c = a*b      #순서7.a*b를 실행
    return c     #순서8. 200결과값 반환 해라

def add(a,b):  #순서2.add 함수 찾음
    c = a+b     #순서3.a+b를 구해서 c변수에 넣음
    print(c)     #순서4.c출력(값30)
    d = mul(a,b) #순서5.mul함수를 부름
    print(d)   #순서8. 200을 출력
                   #순서9. add 함수 끝남
x = 10
y = 20
add(x,y)  #순서1. add함수 호출

#cf.stack(접시가 겹겹히 쌓이는 모양)
#cf.프레임이란 메모리에서 함수와 함수에 속한 변수가 저장되는 독립적인 공간(mul, add, x , y)
# cf.전역 프레임은 파이선 스크립트 전체에서 접근할 수 있어서 전역 프레임이라 부름

## 함수 호출 과정 알아보기
#함수는 스택(stack) 방식으로 호출됨(접시가 겹겹히 쌓이는 모양)
#함수를 호출하면 스택의 아래쪽 방향으로 함수가 추가되고 함수가 끝나면 위쪽 방향으로 사라짐
#프레임은 스택 안에 있어서 각  프레임을 스택 프레임이라고 부름(a = 10,b = 20 ,c =30 ,d= 200)
#전역 프레임은 스크립트 파일의 실행이 끝나면 사라짐(순서 ab> c>d)