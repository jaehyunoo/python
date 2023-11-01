'''
    작성일 : 2023년 11월 1일
    작성자 : 컴소부 202095061 유재현
    설명 : 8.1 키와 값을 가지는 딕셔너리
    
    튜플 = () 리스트 = [] 딕셔너리 = {}
'''

# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. 1. key,value  [key] = value
phone_book1['유재현'] = '010-5314-9787'

print('phone_book1 : ' , phone_book1)  # {'유재현' : '010-5314-9787'}

# 딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {'홍길동' : '010-7899-4545', '유재현' : '010-5314-9787'}

print('phone_book2 : ' , phone_book2)


phone_book3 = {}
phone_book3['유재현'] = '010-5314-9787'
phone_book3['홍길동'] = '010-1234-5243'
phone_book3['주몽'] = '010-1785-3411'
phone_book3['김유신'] = '010-4004-9801'
phone_book3['이순신'] = '010-4046-6933'

print('phone_book3 : ' , phone_book3)

print()
print(":: 전화번호 phone_book3 출력 ::")
# 모든 key를 출력
# dic이름.keys() 는 모든 dic이름의 key들을 전부 출력한다
print(phone_book3.keys())

# 모든 value 출력
# dic이름.values()는 모든 dic이름의 value들을 전부 출력한다
print(phone_book3.values())

# 모든 key, value 출력 
# dic이름.items()는 모든 dic이름의 key와 value들을 전부 출력한다
print(phone_book3.items())

print()
print(":: 전화번호 phone_book3 items()출력 ::")

# key를 name에다가 value를 phone_num 에다가 넣게하기
for name, phone_num in phone_book3.items() :
    print(name, ':', phone_num)
    

print()
print(":: 전화번호 phone_book3[keys]로 접근하여 출력 ::")
for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])
    


print()

print("딕셔너리 작성 시 : (콜론)을 기준으로 key:value 작성")
person_dict = {'name' : '유재현', 'age' : 23, 'class' : '1학년'}

print('이름 : ', person_dict['name']) # 딕셔너리의 'name' 키로 값을 조회하여 출력
print('나이 : ', person_dict['age']) # 딕셔너리의 'age' 키로 값을 조회하여 출력

print(":: 정렬 ::")
# phone_book3를 정렬
# 딕셔너리를 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))


print(':: 키를 기준으로 전체 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0]) # lambda는 이름없는 함수 일회성! 
# lamda x<< x는 매개변수 : x[0]은 0번지값을 돌려주어라는 뜻.
print(sort_phone_book3)

print(':: 값를 기준으로 전체 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1]) # lambda는 이름없는 함수 일회성!
print(sort_phone_book3)


print()
# 항목을 삭제할떄는 key를 입력해주면된다 key를 삭제하면 value도 같이 삭제가 된다.
print(':: 항목 삭제 ::')
del phone_book3['유재현']
print(phone_book3)

print(":: 전체삭제 ::")
phone_book3.clear()
print(phone_book3)












