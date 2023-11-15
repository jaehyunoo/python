'''
    작성일 : 2023년 11월 15일
    작성자 : 컴소부 202095061 유재현
    설명 :  LAB 9-2 : 트위터 메세지를 메세지 처리의 단어 추출
       띄워쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
'''
text = "There's a reason some people are working to make\
    it harder to vote, especially for people of color.\
        It's because when we show up, things change."
        
    
# 띄워쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.

text_list = text.split()
print(text_list)
print('word1 count : ' ,len(text_list))


# 도전문제 9.1
# 회사 이름은 **로 표시
# KT, Samsung, LG, KT

text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'

# 모든 문자를 소문자로 변환
text1 = text.lower()
print(text1)

# 소문자로 바뀐 단어들을 공백으로 구분한다.
text_list = text1.split()
print(text_list)
# 구분된 단어를 검사한다.(판단) => KT 또는 Samsung 또는 LG 또는 KT
# 검사하는 단어가 회사명이면 **으로 바꾼다.
# 아니면 그단어는 그대로 사용한다.

# 바꿀 단어들을 리스트에 저장
company = ['kt','samsung','skt','lg']

# text_list의 길이만큼 반복 실행
for i in range(len(text_list)):
    # text_list의 i번지가 company 리스트 안에있는 원소와 같을경우
    if text_list[i] in company :
        # 회사이름을 **로 변경시켜준다
        text_list[i] = '**'
    # text_list의 i번지가 company 리스트 안에있는 원소와 다를경우
    else :
        # 바꾸어지지않고 그대로 나타낸다
        text_list[i] = text_list[i]

print(text_list)


# 분리된 단어들을 합친다.
print('text : ',' '.join(text_list))


'''
#2
# 소문자로 바뀐 단어들을 공백으로 구분하여 저장한다.
# 리스트에 저장된 단어를 검사한다.(판단) => 단어가 kt 또는 samsung 또는 lg 또는 skt인가?
# 검사하는 단어가 회사명이면 **로 바꾸어 리스트에 저장한다.
# 아니면 그 단어는 그대로 리스트에 저장한다.
# 분리된 단어들을 합친다.

split_text = text1.split()

company = ['kt','samsung','skt','lg']

for i in split_text :
    if i == 'kt'or i == 'samsung' or i == 'lg' or i == 'skt':
        if split_text[i] in company:
            split_text[i] = '**'
        else :
            split_text[i] = split_text[i]

# 분리된 단어들을 합친다.
print('text : ',' '.join(split_text))

'''
    




