'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : P.195 심화문제 7.7
      fruit_list = ["banana","orange","kiwi","apple","melon"]의 리스트가 존재한다
      1) 이 fruit_list에서 가장 길이가 긴 문자열을 찾아서 출력하고 이 리스트에서 삭제하라. 이때 동일한 길이의 문자열이 있을 경우 이들을 모두 삭제해라.
      2) 이 fruit_list와 for 제어문을 이용하여 다음과 같은 문장을 출력하여라.
            banana : 문자열의 길이 6
            orange : 문자열의 길이 6
            kiwi : 문자열의 길이 4
            apple : 문자열의 길이 5
            melon : 문자열의 길이 5
'''

'''
    1) 이 fruit_list에서 가장 길이가 긴 문자열을 찾아서 출력하고 이 리스트에서 삭제하라. 이때 동일한 길이의 문자열이 있을 경우 이들을 모두 삭제해라.
'''

# 문제에서 주어진 리스트
fruit_list =["banana", "orange", "kiwi", "apple", "melon"]
# 가장 긴 문자열의 길이를 찾아서 변수에 저장 (banana와 orange가 문자열 6으로 가장 길다)
maximum = len(max(fruit_list))

print("가장 길이가 긴 문자열 : ", end = " ")
# 리스트를 저장한 변수를 그대로 집어넣으면 반복 중 문제가 발생하므로 리스트내용을 리스트형식으로 써넣는다.
for i in ["banana", "orange", "kiwi", "apple", "melon"]:
    if len(i) == maximum :  # 리스트 항목(i)중 가장 긴 길이(6)을 가진 항목이면
        print(i,end = " ")  # 위 가장 길이가 긴 문자열에 리스트 항목 출력
        fruit_list.remove(i)    # 그리고 fruit_list에서 가장 길이가 긴 문자열을 가진 항목 제거
print() # 줄바꿈
print("fruit_list = ",fruit_list)   # 가장 길이가 긴 항목들을 제외한 fruit_list 출력

'''
      2) 이 fruit_list와 for 제어문을 이용하여 다음과 같은 문장을 출력하여라.
            banana : 문자열의 길이 6
            orange : 문자열의 길이 6
            kiwi : 문자열의 길이 4
            apple : 문자열의 길이 5
            melon : 문자열의 길이 5
'''

fruit_list = ["banana", "orange", "kiwi", "apple", "melon"]

for i in range (0, len(fruit_list)) :
    print(f"{fruit_list[i]} : 문자열의 길이 {len(fruit_list[i])}")
