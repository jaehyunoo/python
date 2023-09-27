'''
    작성일 : 2023년 9월 27일
    작성자 : 컴소부 202095061 유재현
    설명 : 반복문으로 팩토리얼 구하기.
            오늘의 마지막 문제 !
'''

num = int(input("정수를 입력하시오 :"))
fac = 1

for i in range(1,num+1):
    fac = fac * i

print(num, "!은" , fac, "입니다")