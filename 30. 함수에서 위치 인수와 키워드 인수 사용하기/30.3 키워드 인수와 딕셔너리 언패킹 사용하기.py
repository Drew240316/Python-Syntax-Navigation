# >> 키워드 인수와 딕셔너리 언패킹 사용하기
# 딕셔너리 앞에 **(애스터리크 두 개)를 붙여서 함수에 넣는다
# >함수의 인수 이름과, 딕셔너리의 키 이름이 같아야됨.
# > 만약 이름과 개수가 다르면 함수 호출 불가
# > **애스터리스크를 두번 쓰는 이유는 키 - 값 쌍으로 저장되어 있기 때문에
# > 딕셔너리를 한번에 언패킹하면 키를 사용한다는 뜻이 된다
# > **처럼 딕셔너리를 두번 언패킹하여 값을 사용하도록 만들어야 함

def personal_info(name, age, address):
    print('이름: ',name)
    print('나이:', age)
    print('주소: ',address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)






print('################################################################')
# >> 키워드 인수를 사용하는 가변 인수 함수 만들기
# > 함수를 만들 때 def personal_info(**kwargs):와같이 매개변수 앞에 **를 붙여주면
# > 키워드 인수를 사용하는 가변인수 함수를 만들 수 있다.
# > def 함수이름(**매개변수):
# > 매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용함
# > kwargs는 딕셔너리라서 for로 반복할 수 있다.


def personal_info(**kwargs):        #
    for kw, arg in kwargs.items():
        print(kw,':', arg, sep='')



# > 함수를 호출할 때는, 키워드와 인수를 각각 넣거나 딕셔너리 언패킹을 사용한다.

#(아래) 키워드와 값을 직접 넣어 사용
personal_info(name = '홍길동')
personal_info(name = '김길동',age=30)
# 보면, 반복문을 썼다. name이 kw, 값이 arg이다.
personal_info(name = '김길동',age=30, address = '이촌동')

#(아래) 딕셔너리 언패킹을 통해 사용
x = {'name': '홍길동'}
personal_info(**x)
y = {'name' : '김철수', 'age' : 10, 'address' : '이촌동'}
personal_info(**y)

# > 보통 **kwagrs를 사용하면 가변 인수 함수는, 함수 안에서 특정 키가 있는 지 확인한 뒤 해당 기능을 만듬

def personal_info(**kwargs):
    if 'name' in kwargs : #in으로 딕셔너리 안에 특정 키(name)이 있는지 확인하고 출력해주세요라는 말
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:  # in으로 딕셔너리 안에 특정 키(name)이 있는지 확인하고 출력해주세요라는 말
        print('나이: ', kwargs['age'])
