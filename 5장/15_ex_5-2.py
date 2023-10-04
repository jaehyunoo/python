'''
    작성일 : 2023년 10월 4일
    작성자 : 컴소부 202095061 유재현
    설명 : 두 수를 입력 받아
           1. 두 수를 입력 받아 두 수 사이의 합계 출력하기
           2. 두 수 사이의 짝수의 합계 출력하기
           
           심화문제 5.2, 141쪽
           for 또는 while 중 원하는 것 사용
'''
# 1. 두 수를 입력 받아 두 수 사이의 합계 출력하기
num1 = int(input("숫자를 입력하시오 : "))
num2 = int(input("숫자를 입력하시오 : "))

# 두수 중 큰 수 작은 수 구분
a = min(num1,num2)
b = max(num1,num2)

total = 0 # 합계를 저장할 변수 초기화
total2 = 0

for i in range(a,b+1):   # num1부터 num2까지의 숫자를 더하기
    
    total = total + i #더하는숫자를 i만큼 증가시킨다
    
#format문을 사용하기
print(f"{a}부터{b}까지의 합은{total}입니다.")

# 2.두 수 사이의 짝수의 합계 출력하기
for i in range(a, b+1):
    if i % 2 == 0:  # 사이의수 i가 짝수 일때 만
        total2 = total2 + i #더하는숫자를 i만큼 증가시킨다

print(f"{a}부터{b}까지의 짝수들의 합은{total2}입니다.")