'''
    작성일 : 2023년 10월 4일
    작성자 : 컴소부 202095061 유재현
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
            
    Test word : programming
'''
# 사용자로부터 단어를 입력받는다
word = input("단어를 입력하세요 :")

# ":: break1 :: "을 출력한다
print(":: break1 :: ")

# word를 이용한 for 반복문을 실행한다
for i in word :
    # 입력된 단어에 a 또는 e 또는 i 또는 o 또는 u 를 입력되어 있을 경우에
    # 반복문이 끝난다
    if i == 'a' or i  == 'e' or i == 'i' or i =='o' or i == 'u' :
        break 
    # 반복문에 속하면 a,e,i,o,u중 첫 번째로 나온 곳 앞까지 출력
    # 반복문에 속하지않는다면 전체 word가 출력된다
    else :
        print(i,end='')
        
        
        
print(":: break2 :: ")


for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] : #모음을 만나면 반복중지
        break # 반복을 중단한다. 반복을 빠져 나간다.
    
    else :
        print(i,end='') 


print()


print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] : 
        continue    # 반복의 시작으로 돌아갑니다. / 반복을 계속 한다.
    print(i,end='') # if 문에있는 알파벳를 제외한 word가 나온다