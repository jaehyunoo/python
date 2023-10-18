'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : P.168 심화문제 6.5
       섭씨온도를 0도에서 50도까지 10도 단위로 증가시키면서 이에 해당하는 화씨온도를 출력하는 프로그램을 작성하시오.
       이를 위하여 섭씨온도를 인자로 받아서 화씨온도를 반환하는 cel2ah() 함수를 만들도록 하여라.
'''
# 섭씨온도(celsius)를 인자로 받아서 화씨온도를 반환하는 cel2ah함수 정의
def cel2ah(celsius):
    fahrenheit = (9/5) * celsius + 32   # 섭씨온도를 화씨온도로 변환하는 공식
    return fahrenheit   # 화씨온도값을 ce12ah(celsius)값으로 반환한다.

for celsius in range(0, 51, 10):    # range(시작값, 마지막값+1, 증가값) 섭씨온도를 0부터 10씩증가시켜 50도가 될 때까지 반복
    
    fahrenheit = cel2ah(celsius)    # 섭씨온도를 화씨온도로 반환
    print(f"{celsius}도 섭씨는 {fahrenheit}도 화씨입니다.") # 결과를 출력