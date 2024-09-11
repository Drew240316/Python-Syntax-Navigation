# 숫자가 같은지 확인
a = 10 != 5
print(a)
# 문자열이 같은지 확인 (대문자, 소문자도 전부 확인함)
print('python' == 'PyTHON')
# 부등호 사용하기
print(10>20)
#객체가 같은지 확인하기
##같다는 == 다르다는 !=가 있는데, 왜 is, is not을 만들었을까?
##is, is not도 같다, 다르다 라는 뜻이지만 is is not은 객체를 비교한다
##a = 1 is 1.0를 비교하면 false가 나옴
##그 이유는, 1은 정수고, 1.0은 실수 이기 때문이다.
## 가끔 syntaxwarning is with a literal. did you mean "=="?이라고나온다

# 정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인했는가?
#id 함수를 사용gkwk
#id 함수는 객체의 고유한 값인 메모리 주소를 구한다.
print(id(a))