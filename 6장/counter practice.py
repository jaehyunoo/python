def print_counter():
    print("counter =", counter)
    
counter = 100   # 전역 변수 -> 전체 영역에서 적용되는 변수
print_counter()

# 출력 결과 ? counter = 100

def print_counter():
    counter = 200 # 지역변수 -> 지정된 영역에서 적용되는 변수
    # 전역 변수로 바꾸려면 변수앞에 global을 붙인다.
    print("counter =", counter)

counter = 100 # 전역변수
print_counter()
# 출력 결과 ? counter = 200


def order(num, pickle, onion):
    print("햄버거 {0} 개 - 피클 {1}, 양파{2}".format(num,pickle,onion))

order(1) # 올바르지 않음 매개변수와 인수 값 동일해야한다