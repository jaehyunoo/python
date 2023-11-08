'''
    작성일 : 2023년 11월 8일
    작성자 : 컴소부 202095061 유재현
    설명 : 집합 set()
'''
# () 튜플 {} 딕셔너리(사전)
# 집합 => 순서가없음, 내가 입력한 순서대로 출력을 해주지않는다.
# *** 집합은 중복을 허용하지 않는다. ***
# 비어있는 집합 생성( set () )
# 집합에서 사용할 수 있는 연산 : 합집합 연산 A | B 메소드 A.union(B) (209페이지 참조!!) -> 시험 예상문제


number = set()

# 숫자 3개로 이루어진 집합
number1 = {2,1,3}
print("집합 : ", number1)

# 리스트로부터 집합 생성 => 리스트를 집합으로 바꾸기 set ([리스트])  
number2 = set([1,2,3,1,2])  # 중복된 숫자는 하나만 출력된다.
print("집합 : ", number2)

# 문자열을 집합으로 생성
text1 = set("asdfasdf") # 철자하나씩 떼어져 중복된 철자는 제외하고 하나의 철자(알파벳)만 출력.
print("text1 : ", text1)

numbers = {2,4,5,1,2}
if 1 in numbers :   # numbers집합안에 1이 있을경우에는
    print("집합에 1이 있습니다.")
    
# 집합은 순서가 없어서 index로 접근이 불가능하다.
# 반복문으로 접근하여 출력 가능하다.
numbers = {9,1,5,2,4,7,6,3,4,9,1}

for num in numbers :
    print(num, end =' ')
    
print ()    # end가 위에있기때문에 공백출력 한번해줘야함

# 정렬 후 출력하기 ( sorted () )
for num in sorted(numbers) :
    print(num, end =' ')

print()
    
for num in sorted(text1) :
    print(num, end =' ')

print ()

# 추가하기 ( 집합에 추가할때에는 집합명.add( ) )
numbers.add(100)
print(numbers)
for num in sorted(numbers):
    print(num,end =' ')
    
print ()
    
# 삭제(제거)하기 ( 제거할 때에는 집합명.remove( ) )
numbers.remove(100)
print(numbers)
