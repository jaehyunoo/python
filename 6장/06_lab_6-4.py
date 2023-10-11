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
import random  # 랜덤 함수를 가져옵니다

def get_random_numbers():
        random_numbers = [random.randint(10,99) for i in range(10)] # 10에서 99사이의 숫자 중 10개를 무작위 숫자로 리스트를만듭니다.
        return random_numbers   # 무작위 숫자 리스트를 돌려줍니다.

def find_max_or_min(random_numbers,option): 
        if option == 'max':
            result = max(random_numbers)  # max 선택 시, 리스트 내에서 최대값 찾아 result에 저장
        if option == 'min':
            result = min(random_numbers)    # min 선택 시, 리스트 내에서 최소값 찾아 result에 저장
        
        return result   # 이 결과 값을 돌려줍니다.

while True: # 무한반복 시키기.
    
    random_numbers = get_random_numbers()   # 무작위 숫자 리스트를 생성
    option = input("최대값을 알고싶으시면 max 최소값을 알고싶으시면 min을 입력하시오")  # 사용자로부터 최대값을 알고싶은지 최소값을 알고싶은지 입력받는다.
    
    result = find_max_or_min(random_numbers, option)    # 사용자가 입력한 것에따라 리스트 내에 최대값 또는 최소값을 찾습니다.
    
    if result is not None:  # 결과 값이 None이 아닌 경우
        if option == 'max': 
            print(f"최대값은 {result}입니다.")  # max 입력시 최대값 출력
    
        elif option == 'min':
            print(f"최소값은 {result}입니다.")  # min 입력시 최소값 출력
    
    else :
        print("잘못된 입력입니다. max 또는 min을 입력해주세요.") # max min이 아닌 다른 값을 넣을경우 메세지 출력.
        


        

