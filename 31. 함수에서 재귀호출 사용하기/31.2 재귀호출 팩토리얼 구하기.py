# 팩토리얼은 1부터 n까지 양의 정수를 차례대로 곱한 값이며 !(느낌표) 기호로 표기함
# 예를들어 오팩토리얼은 얼마인지 봤을 때, 5!= 5*4*3*2*1 이렇게 된다.

def factorial(n):
    if n == 1:    #n이 1일 때
        return 1  #1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1) #n과 factorial 함수에 n-1을 넣어서 반환된 값을 곱합

print(factorial(5))

