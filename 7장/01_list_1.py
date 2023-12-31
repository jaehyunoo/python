'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : 리스트 만들기
'''

# 과일 리스트 만들기
fruits = ['딸기','사과','바나나']
print("과일 목록 : ",fruits)


# 수박 추가 => append() 메소드 사용 - append메소드는 마지막에(끝에) 추가된다. # 시험 문제 출제예상
fruits.append("수박")
print("과일 목록(수박 추가) : ",fruits)

# 망고추가 => append() 메소드 사용
fruits.append("망고")
print("과일목록(망고추가) : ",fruits)

# 포도 추가 => + 연산자 사용 : 연결연산자의 역할 --> append와 같이 맨 마지막에 추가된다.
fruits = fruits + ["포도"]      # 포도를 더해서 fruits에 저장
print("과일 목록 (포도 추가) : ",fruits)

# 문제 예) 아래 코드를 보고 출력 결과를 입력하세요.
num = [1,2,3] + [4,5,6] # 리스트에서 + 는 연결 연산자이다. 숫자끼리 더하지 말고 리스트에 추가하는 역할이다.
print("숫자 리스트 : ", num)

# * 연산자 => 리스트를 n번 반복한다. 아래 코드의 출력결과 = 숫자리스트 * 3 :  [1, 2, 3, 1, 2, 3, 1, 2, 3]
num = [1,2,3] * 3
print("숫자리스트 * 3 : ", num)

# in 연산자 => 포함되는가 ?   리스트안에있으면 True 없으면 False로 나옴
print("과일 목록에 망고가 있나요?", "망고" in fruits)


'''
인덱스를 사용하여 리스트 항목에 접근하기 P.178
'''
# 과일리스트에 있는 과일의 개수 ?
print("과일 리스트에있는 과일의 개수는 ?",len(fruits))
# 과일 중 제일 첫 번째 과일은?
print("과일 중 제일 좋아하는 과일은 ?",fruits[0])

# 과일 리스트 중 제일 마지막 과일은 ? 0부터시작이기 때문에 6번째 자리는 5가된다 [0,1,2,3,4,5] 또는 마지막을 찾기 위해서는 -1을 입력.
print("과일 중 제일 마지막 과일은 ?",fruits[-1])

# 과일 중 가장 큰 과일은 ?
print("과일 중 가장 큰 과일은 ?(사전식 순서)",max(fruits))

# 과일 중 가장 작은 과일은?
print("과일 중 가장 작은 과일은 ?(사전식 순서)",min(fruits))

# 정렬
fruits.sort() # 오름차순으로 정렬
print("오름차순 정렬 : ", fruits)

fruits.sort(reverse=True)   # 내림차순으로 정렬
print("내림차순 정렬 : ",fruits)

'''
    리스트를 원하는 모양으로 자르는 슬라이싱 P.179
'''
# 리스트 함수에서 필기문제 출제 유력

print("과일 목록 : ", fruits)
print("과일 리스트 중 2,3,4번 과일은? ", fruits[1:4]) # 1번지[두 번째] ~ 4번지[다섯 번째] 앞까지 (1번지부터 3번지까지)
print("과일 리스트 중 1,2,3번 과일은? ", fruits[0:3]) # 0번지 [첫 번째] ~ 3번지[네 번째] 앞까지 (0번지부터 2번지까지)
print("과일 리스트 중 1,2,3번 과일은? ", fruits[:3]) # 처음부터 2번지 까지 ★ : 앞에 숫자를 안적을경우 = 처음 부터(0번지 부터)
print("과일 리스트 중 3번과일부터 마지막 과일까지는? ", fruits[2:5]) # 2번지[세 번째] ~ 5번지[여섯 번 째] 앞까지 (2번지 부터 4번지까지)
print("과일 리스트 중 3번과일부터 마지막 과일까지는?", fruits[2:]) # 2번지[세 번째]부터 마지막 번지과일까지 출력
print("과일 리스트 중 1,3,5번 과일은?", fruits[::2]) # 처음부터 끝까지 리스트 중에서 2씩 증가하면서 출력
print("과일을 거꾸로 출력",fruits[::-1]) # 기존의 리스트를 역순으로 출력

'''
    리스트의 원소 값을 자유롭게 조작해 보자.
'''
print()
print("과일 목록 : ",fruits)

# 원하는 위치에 "두리안" 추가 => insert() 메소드 사용
fruits.insert(3,"두리안") # 3번지 자리에 추가
print("과일 목록 : ",fruits) # 두리안이 3번지에 추가된 후 리스트 재출력 => 원래 3번지에있는 항목부터는 뒤로 1번지씩 밀려난다.

# 위치 찾기 => index()메소드 사용
print("사과의 위치는",fruits.index("사과")) # 위치는 번지 수로 나온다.

# 사과를 마지막에 추가
fruits.append("사과") # append는 리스트 맨 마지막에 추가하는 메소드
print("과일 목록 : ",fruits)

# 사과의 개수 출력 => count()메소드 사용
print("사과의 개수는?", fruits.count("사과"))

'''
    리스트의 항목 삭제
'''
print()

# 사과 삭제 => remove() 메소드 사용
fruits.remove("사과")   # 사과가 여러개인 경우 처음 만나는 사과만 삭제
print("과일 목록(사과 삭제 후) : ",fruits)

# 항목 삭제 => pop() 메소드 사용
fruits.pop() # pop은 젤 마지막 항목을 삭제 => ()안에 즉 메소드 안에 아무것도 사용하지않는다
print("과일 목록(마지막 과일 삭제) : ",fruits)

# del() 키워드 => 포도 삭제
del fruits[0] # 0번지 항목 삭제
print("과일목록 : (포도(0번지)삭제)", fruits)