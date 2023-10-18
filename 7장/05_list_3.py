'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : 리스트의 객체 생성과 참조
'''
# fruits1 변수에 저장되는 리스트 생성
fruits1 = ["딸기", "수박", "바나나"]

# 실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사된다.
fruits2 = fruits1

print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

fruits2[1] = "망고" # fruits2 리스트의 1번지 과일을 망고로 바꾸면

print("fruits1 : ", fruits1)    # fruits1과 fruits2 둘 다 1번지 내용이 망고로 바뀐다
print("fruits2 : ", fruits2)    # 왜냐하면 주소를 참조하기 때문이다.(같은 주소)

# 주소 확인 => 메모리 위치 정보 알아보기 id()함수 사용
print("fruits1의 id : ", id(fruits1))
print("fruits2의 id : ", id(fruits2))   # fruits1,fruits2 두 리스트의 id 정보(주소 값)가 같다

'''
    리스트 내용 복제하기    list()함수
'''
# 내용 복제 1
fruits2 = list(fruits1)  # 내용복제(배정) 내용복제할때는 list 무조건 써주기.
print(":: 내용 복제 후 1 ::")
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

print("fruits1의 id : ", id(fruits1)) 
print("fruits2의 id : ", id(fruits2))   # fruits1,fruits2 두 리스트의 id 정보(주소 값)가 다르다.

# 내용 복제 2
fruits3 = fruits1[:] # fruits1의 리스트 처음과 끝까지 복제

print(":: 내용 복제 후 2 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)

print("fruits1의 id : ", id(fruits1)) # id 정보가 다르다
print("fruits3의 id : ", id(fruits3))

fruits3[0] = "수박" # fruits3 리스트의 0번지 항목을 수박으로 바꾼다
print(":: fruits3의 0번지에 수박으로 내용 바꾼 후 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)

