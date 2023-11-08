'''
    작성일 : 2023년 11월 8일
    작성자 : 컴소부 202095061 유재현
    설명 : 집합의 연산
'''

# 비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}
print("num1 == num2 ? ", num1 == num2) # 같으면 True 다르면 False 출력

# 6개의 숫자로 집합 생성
num_set = {1,4,6,3,7,4}
print("num_set : ", num_set) # 중복된 숫자를 제외하고 출력
print("num_set 길이 : ",len(num_set)) # 중복을 제외하고 집합의 길이 출력 (5개)
print("num_set 중 가장 큰값 : ",max(num_set)) # 집합안에있는 것중 가장 큰 값 출력
print("num_set 중 가장 작은값 : ",min(num_set)) # 집합안에있는 것중 가장 작은 값 출력
print("num_set 중 가장 합계 : ",sum(num_set)) # 중복된 것은 하나만 계산하여 합을 구한다.


num1 = {1,2,3}
num2 = {3,4,5}

# 합집합 
print("num1 | num2 : ", num1 | num2) # 합집합 연산자 : | , 중복 허용하지않음
print("num1.union(num2) : ", num1.union(num2)) # 합집합 메소드 .union() , 중복허용하지않음

# 교집합
print("num1 & num2 : ", num1 & num2) # 교집합 연산자 : &
print("num1.intersection(num2) : ", num1.intersection(num2)) # 교집합 메소드 .intersection()

# 차집합
print("num1 - num2 : ", num1 - num2) # 차집합 연산자 : -
print("num1.difference(num2) : ", num1.difference(num2)) # 차집합 메소드 .difference()

# 대칭차집합
print("num1 ^ num2 : ", num1 ^ num2) # 대칭차집합 연산자 : ^
print("num1.symmetric_difference(num2) : ", num1.symmetric_difference(num2)) # 대칭 차집합 메소드 .symmetric_difference()