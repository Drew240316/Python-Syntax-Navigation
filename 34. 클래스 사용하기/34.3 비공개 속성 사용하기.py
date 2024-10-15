#class Person:
    #def __init__(self, name, age, address, wallet):
        #self.name = name
        #self.age = age
        #self.address = address
        #self.__wallet = wallet  #변수 앞에 __를 붙여서 비공개 속성으로 만듬

#maria = Person('마리아','20','서울시 서초구 반포동',10000)
#maria._wallet -= 10000 #클래스 바깥에서 비공개 속성에 접근하면 에러가 발생

#####################
# 비공개 속성 사용하기 : 비공개 속성은 클래스 안의 메서드에서만 접근 가능
class Person :
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  #변수 앞에 __를 붙여서 비공개 속성으로 만듬

    def pay(self,amount):
        self.__wallet -= amount  #비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아',30,'서초구 반포동',10000000)
maria.pay(3000)   #함수를 호출할 때 3000을 위에 def pay의 amount 인스턴스에 넣음


#주로 언제 사용? 중요한 값인데 바깥에서 함부로 바꾸면 안될 때 비공개 속성을 주로 사용
# 비공개 속성을 바꾸는 경우는 클래스의 메서드로 한정함
# 지갑에 든 돈이 얼마인지 확인하고 돈이 모자라면 쓰지 못하는 식으로 만듬

def pay(self, amount):
    if amount >self.__wallet:
        print("돈이 모자라네")
        return
    self.__wallet -= amount