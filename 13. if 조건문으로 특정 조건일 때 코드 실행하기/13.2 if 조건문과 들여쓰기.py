# if 조건문은 들여쓰기가 매우 중요하다.


#x = 10

#if x == 10:
 #   print("x에 들어있는 숫자는? ")
  #      print("10입니다.")        # IndentationError : unexpected indent 가 뜬다.
                                # 들여쓰기 오류: 예기치 않은 들여쓰기

x = 5

if x == 10:
    print("x에 들어있는 숫자는? ")
print("10입니다.")     # 전혀 다른 값이 나옴.

