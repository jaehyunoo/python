'''
    작성일 : 2023년 11월 1일
    작성자 : 컴소부 202095061 유재현
    설명 : LAB 8-1 편의점 재고 관리 프로그램
    
'''

items = { "커피음료": 7, "펜" : 3, "종이컵" : 2, "우유" : 1, "콜라" : 4, "책" : 5}

# 물건의 목록을 출력
# print(items.keys())
print("제풀 목록 : ", end = ' ')
for key in items.keys() :
    print(key, end= ', ')
print()

# 물건의 이름을 입력 받아 재고를 출력한다.
name = input("물건의 이름을 입력하시오 : ")
print("재고 : ", items[name])