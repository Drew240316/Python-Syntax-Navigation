(아래) 클래스 정의 (인스턴스 변수 정의 및 인스턴스 메서드 정의)
class Person:
    def __init__ (self, name, age, address) :   #클래스 외부에서 **전달받은 값(매개변수) :   호출 부분의 maria = Person('마리아',20,'서울특별시 마포구')이 차례대로 들어가는 것임
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address


    def greeting(self) :
        print('{0}저는 {1}입니다'.format(self.hello, self.name))


#(아래) 호출
maria = Person('마리아',20,'서울특별시 마포구')
maria.greeting() #안녕하세요. 저는 마리아입니다.

print('이름: ',maria.name)  #마리아
print('나이: ',maria.age)   #20
print('주소: ',maria.address) #서울시 서초구 반포동


# (주의) 인스턴스를 만들 때 값 받기
# 클래스 내부에서는 self.(클래스 외부에서 **전달받은 값(매개변수) )이였다면, 클래스 바깥에서 속성에 접근할 때는 인스턴스변수명.속성 형식으로 접근한다.
# maria.name, maria.age, maira.addrees의 값을 출력해보면 Person으로 인스턴스를 만들 때 넣었던 값이 출력됨
# 인스턴스를 통해 접근하는 속성을 인스턴스 속성(변수)라고 부른다