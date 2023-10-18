'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 :  P 143 심화문제 5.7
        암스트롱 수란 xyz로 표시되는 세 자리의 정수 중에서 각 자리의 수를 세제곱한 수의 합과 자신이 같은 수를 말하며 다음과 같은 조건을 만족한다.
        구체적인 예를 들면 153은 1 + 125 + 27의 합으로 구성될 수 있는데 이러한 수가 암스트롱 수이다. 세 자리 정수들 중에서 모든 암스트롱
        수를 구하여 다음과 같이 출력하여라.
'''

print("세 자리의 암스트롱 수 : ")

# 세자리 정수의 범위 (100~999) 정하기
for num in range(100,1000):
    
    x = num // 100 # 세 자리 정수중 백의자리 숫자는 x
    y = (num % 100) // 10 # 세 자리 정수중 십의자리 숫자는 y
    z = (num % 100) % 10 # 세 자리 정수중 일의자리 숫자는 z
    
    sum1 = x * 100 + y * 10 + z # 세 자리 정수의 값은 sum1
    sum2 = x**3 + y**3 + z**3 # 세 자리 정수의 각 자리 수의 3제곱의 합은 sum2
    
    if  sum1 == sum2: # 세 자리 정수의 값과 세 자리 정수의 각 자리 수의 3제곱의 합이 같으면
        print(num)      # 위 조건에 맞는 세 자리 정수 출력
        
