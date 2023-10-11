'''
    작성일 : 2023년 10월 11일
    작성자 : 컴소부 202095061 유재현
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.
    
    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 돌려준다
    (메인)
        1.무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
'''
import random   # 랜덤 함수 불러오기

# 함수 선언

# 두 값을 전달받아 매개변수에 저장
def max_or_min(numbers, maxmin): 
    if maxmin == 'max':             # maxmin이 max이면 result는 최대값
        result = max(numbers)
    if maxmin == 'min':             # maxmin이 min이면 result는 최소값
        result = min(numbers)
        
    
    return result                   # result 값을 호출한 곳으로 돌려준다.

while True :        # 무한반복
    
    random_numbers = [random.randint(10,99) for i in range(10)]     # 10에서 99사이의 10개 랜덤숫자 리스트 생성
    
    print("생성된 랜덤숫자 리스트", random_numbers)                   # 생성된 리스트 출력
    
    maxmin = input("최대값을 알고싶으시면 max 최소값을 알고싶으시면 min을 입력하시오")  # 사용자에게 최대값을 알고싶은지 최소값을 알고싶은지 입력받기.
    
    result = max_or_min(random_numbers, maxmin)       # 입력받은 값 max 또는 min과 생성된 리스트를 가지고 함수 호출
    
    
        
    if maxmin == 'max':           # max를 입력하였을 때 최대값 출력
            print(f"최대값은 {result} 입니다.")
        
    if maxmin == 'min':         # min을 입력하였을 때 최소값 출력
            print(f"최소값은 {result} 입니다.")
   
        

        

