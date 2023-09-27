'''
    작성일 : 2023년 9월 27일
    작성자 : 컴소부 202095061 유재현
    설명 : 터틀 그래픽으로 여러 개의 원을 그려보자.
            
'''

import turtle as t

# 원 하나 그리기
#t.circle(100) # 반지름이 100인 원(반지름)

for count in range(5) :
    t.circle(100)
    t.left(360 / 10)

t.mainloop()    #종료
# t.done    #종료