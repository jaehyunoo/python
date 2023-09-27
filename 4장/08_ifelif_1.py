'''
    작성일 : 2023년 9월 27일
    작성자 : 컴소부 202095061 유재현
    설명 : 점수를 입력받아 학점을 출력하시오.
            90~100 : A학점
            80~89 : B학점
            70~79 : C학점
            60~69 : D학점
            0~59 : F학점
''' 
# 점수를 입력받는다.
score = int(input("점수를 입력하시오: "))

# 판단.  elif 랑 if를 반복하는것과는 차이가 있다. elif : 나머지 중에서 만약에 
# 이 코드는 논리 오류가 발생한다. - 300점 입력하면 A학점으로 나온다.
print("::: 첫 번째 성적처리 :::")
if 90 <= score :
    print("A학점")

elif 80<= score :
    print("B학점")

elif 70 <= score :
    print("C학점")

elif 60 <= score :
    print("D학점")

else :
    print("F학점")

print() #빈줄 출력

# 정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력입니다.
'''
            90~100 : A학점
            80~89 : B학점
            70~79 : C학점
            60~69 : D학점
            0~59 : F학점
'''
print("::: 두 번째 성적처리 :::")

if (90 <= score <= 100) :
    print("A학점")


elif (score >= 80 and score < 90):          # C : score >= 80 && score <=89
    print("B학점")

elif (70<= score <= 79):
    print("C학점")

elif (60<= score <= 69):
    print("D학점")

elif (0<= score <= 59):
    print("F학점")

else :
    print("점수를 잘못 입력하셨습니다.")

print()

# 점수는 무조건 0~100점 사이입니다. - 아니면 잘못된 입력입니다.
print("::: 세 번째 성적처리 :::")

if 0 <= score <= 100 :

    if 90 <= score :
        print("A학점")

    elif 80<= score :
        print("B학점")

    elif 70 <= score :
        print("C학점")

    elif 60 <= score :
        print("D학점")

    else : #A,B,C,D 학점이 아니면
        print("F학점")

else : # 0~100 사이의 정수가 아니면
    print("점수를 잘못 입력하셨습니다.")

