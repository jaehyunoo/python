'''
    작성일 : 2023년 11월 8일
    작성자 : 컴소부 202095061 유재현
    설명 : 심화문제 8-6 (P.217)
'''

# 튜플을 요소로가지는 student_tuple 리스트 생성
student_tuple = [("211101", "강이안", "010-123-1111"), ("211102", "박동민", "010-123-2222"), ("211103", "김수정", "010-123-3333")]

# 이를 이용하여 (학번 : 이름)의 딕셔너리를 만들어 출력하여라.
student_dict = {} 
# 반복문 활용
for student_info in student_tuple : 
    student_dict[student_info[0]] = student_info[1]
     

print(student_dict)

# 이를 이용하여 학번으로 조회를 할 경우 다음과 같이 학번, 이름과 전화번호가 출력되도록 하여라.

# 학번 입력받기
id = input("학번을 입력하시오 : ")

# 입력받은 학번이 student_dict 안에있을때
if id in student_dict:
    # name은 stdent_dict[id]의 값입니다.
    name = student_dict[id]
    # 반복문
    for student_info in student_tuple:
        # student_info의 0 번지가 입력받은 id와 같을 때 
        if student_info[0] == id:
            print(f"{id} 학생은 {name}이며, 전화번호는 {student_info[2]}입니다.")
            
            
            