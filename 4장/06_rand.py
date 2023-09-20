'''
    작성일 : 2023년 9월 20일
    작성자 : 컴소부 202095061 유재현
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.

            random함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보

'''
import random           #random 함수 가져오기.(포함 시키기.)

print("가위바위보 게임을 시작합니다")
rsp = random.randrange(3)   #랜덤으로 0,1,2 생성

# 가위 바위 보 출력

if rsp == 0 :
    print("가위")
elif rsp == 1:
    print("바위")
else :
    print("보")
    