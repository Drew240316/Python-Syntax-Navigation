# random 함수는 난수 생성
# import를 해야한다.
# random.randint(1,4) 함수는 생성할 범위를 지정하여, 임의의 숫자가 나온다

import random
print(random.randint(1,4))


# 생성된 난수가 3이 나오면, 반복을 끝내는 함수를 만들어라


import random

i = 0

while i != 3:
    i = random.randint(1,6)
    print("실행 ->",i)


