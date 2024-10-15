# 사용자가 입력한 숫자 만큼 True를 출력하고 싶다. while을 활용해라!

#count = int(input("입력하시오 숫자 :"))


#i = 0

#while True:
    #print("True", i)
    #i += 2
    #if i == 100:
        #break


# 사용자가 입력한 숫자까지 홀수를 출력해주세요!for문 사용해주세요

a = int(input("입력 :"))

for i in range(a+1):
    if i % 2 ==0:
        continue
    print(i)
