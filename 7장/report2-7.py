'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : P.195 심화문제 7.2
      다음과 같은 list1, list2가 있을 경우 이중 for 루프를 사용하여 list1과 list2의 각 원소를 곱한 후 원소의 곱셈을 아래와 같이 출력하시오.
'''
# 문제에 제시된 리스트 생성
list1 = [3,5,7]
list2 = [2,3,4,5,6]
# list1과 list2의 각 항목을 곱한 결과를 출력하기위한 이중 for루프
for list1_num in list1: # list1의 각 항목를 반복
    for list2_num in list2: # list2의 각 항목를 반복
        result = list1_num * list2_num # 두 항목을 곱한결과를 result변수에 저장
        print(f"{list1_num} * {list2_num} = {result}") # 결과 출력