'''
    작성일 : 2023년 10월 11일
    작성자 : 컴소부 202095061 유재현
    설명 : 함수의 디폴트 인자.
'''
def order(num, pickle, onion) :
    print("햄버거{}개 - 피클{}, 양파{}".format(num, pickle, onion))
    
# order(1) # 매개변수개수(3개)와 인자개수(1개)가 일치하지않아서 오류 발생

# 인자가 부족한 경우 기본값을 넣어 주는 것 => 디폴트 인자

def order2(num, pickle = '기본', onion = '기본') :
    print("햄버거{}개 - 피클{}, 양파{}".format(num, pickle, onion))


order2(2)
order2(1, pickle = '뺌', onion = '기본')