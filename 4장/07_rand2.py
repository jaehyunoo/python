'''
    작성일 : 2023년 9월 20일
    작성자 : 컴소부 202095061 유재현
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.

            random함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
            
            두명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다
'''
import random           #random 함수 가져오기.(포함 시키기.)

print("가위바위보 게임을 시작합니다")


player1 = input("Player1의 이름 : ")
player2 = input("Player2의 이름 : ")
rsp1 = random.randrange(3)   # player 1의 랜덤 수 
rsp2 = random.randrange(3)      #player 2 의 랜덤 수
# player1 가위 바위 보 출력
print(player1, " : ",end='')
if rsp1 == 0 :
    print("가위")
elif rsp1 == 1:
    print("바위")
else :
    print("보")

# player2의 가위 바위 보 출력
print(player2, " : ", end='')
if rsp2 == 0 :
    print("가위")
elif rsp2 == 1:
    print("바위")
else :
    print("보")

# 승자 판단하여 출력 ( 1번째 방법 )
if rsp1 == rsp2 :
    print("비겼습니다")
elif rsp2 - rsp1 == 1 :
    print("Player2가 이겼습니다")
elif rsp1 - rsp2 == 1 :
    print("Player1이 이겼습니다")
elif rsp2 - rsp1 == 2 :
    print("Player1이 이겼습니다")
else : 
    print("Player2가 이겼습니다")

## 승자판단 (2번째 방법)
## if rsp1 == rsp2 :
##  print("비겼습니다.")
## elif (rsp2 - rsp1 == 2) or ( rsp1 - rsp2 == 1)  :
##  print("Player1이 이겼습니다")
## else :
##  print ("Player2가 이겼습니다")
    