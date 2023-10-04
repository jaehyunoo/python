'''
    작성일 : 2023년 10월 4일
    작성자 : 컴소부 202095061 유재현
    설명 : 사용자가 입력하는 숫자의 합을 계산해보자.
            교재 133 페이지
'''


# 시작 값은 입력받을거고 합계의 시작은 0으로 설정
total = 0

# 변수 answer 값은 yes
answer = 'yes'

# 대답이 yes가 나올 때마다 반복하고 yes가 나오지 않을 경우 종료.
while answer == 'yes':
    # while문을 시작하는 숫자 입력하기
    num = int(input("숫자를 입력하시오 : "))
    # yes가 나오지 않을 때 까지 num을 계속 더하기 위한 식을 만들기
    total = total + num
    # 한 번 숫자를 입력하였을 때 계속 숫자를 더할 것인지 멈출 것인지 물어보기
    # yes를 입력할 경우에는 계속 숫자를 입력받고 no를 입력할 경우에는 while문이 끝
    answer = input("계속?(yes or no) : ")
    
 #브레이크문   if answer == 'no' :
 #                     break
 
# while문이 끝났을 경우에 while문 동안 입력받은 숫자합계 입력받기
print("합계는 : ", total)
