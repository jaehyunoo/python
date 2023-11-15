'''
    작성일 : 2023년 11월 15일
    작성자 : 컴소부 202095061 유재현
    설명 :  문자열
'''
# 문자형식도 주소를 가지고있다 -> 리스트와같다, 0번지부터 시작한다.

# 문자열 슬라이싱
s = 'Happy Day!'
print(s[0]) # 0번지만 잘라서 보여준다.
print(s[6:10]) # 6번지부터 ~ 9번지까지 (Day!)
print(s[:-2]) # 뒤에서 두번째 y앞까지 즉 a까지 출력된다. 0부터 뒤에서 2번째 앞까지


# 문자열 분리 : split()은 ()안에 들어가는것은 무엇을 기준으로해서 분리할지 적는 공간이다.
s = 'Welcome to Python'
print(s.split()) # 공백을 기준으로 분리해서 리스트 형식으로 출력된다 ['Welcome', 'to', 'Python']


s = '2023.11.15'
print(s.split('.')) # 분리기준은 .이다

s = 'Hello, World!'
print(s.split(',')) # 분리기준은 ,이다

s = 'Hello, World!'
print(s.split(', ')) # 분리기준은 ,공백 이다

# 공백 제거 : strip()
s = 'Welcome, to, Python, and , bla, bla     '
print(s.strip())
print([x.strip() for x in s.split(',')]) # s에있는 것을 쉼표를 가지고 분리한 것들을 x에담아서 x에서 공백을 제거한다.



print(list('Hello, World!')) # 이 문자열을 리스트로 단어,공백,쉼표를 하나하나 따로따로 리스트에 저장시킨다
                                # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


# 문자열 연결 : join()
print(','.join(['apple','grape','banana'])) # ,를 붙여서 연결하라.
print('-'.join('010.1234.5678'.split('.')))  # .으로 먼저 구분시켜 -로 고친다.


# .을 -로 바꾸기 .replace(바뀌기 전 문자, 바뀌어질 문자)
print('010.1234.5678'.replace('.','-')) # 문자.을 문자-으로 바꾸는 방법 2 



s = 'hello world!'
print(s)

# s에 저장된 문자열을 리스트로 문자열 분리 시켜 slist에 저장.

slist = list(s)
print(slist)

# 분리된 문자를 다시 합치기
print(''.join(slist)) # slist를 아무것도 없이 합쳐지기 => 원래상태로 되돌아감(공백도 같이)


# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Have a Happy day'
print(a_string)

# 문자열 자르기
word_list = a_string.split()    # 단어들만 가지고 word_list에 저장된다 줄바꿈과 탭은 리스트에나오지않는다
print(word_list)            # ['Today', 'as', 'well,', 'Have', 'a', 'Happy', 'day']

# 다시 합치기 : 문자열을 자르고 다시 합치면 줄바꿈과 탭이 삭제된다.
refined_string = " ".join(word_list)
print(refined_string)

# 대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s)
print(s.lower()) # .lower() 은 전부 소문자로 바꿈
print(s.upper()) # .upper() 은 전부 대문자로 바꿈

# 공백제거 strip()
s = '       Hello, World!     '
print(s.strip()) # 왼쪽, 오른쪽 모든 공백을 제거함
print(s.lstrip()) # 왼쪽 공백만 삭제
print(s.rstrip()) # 오른쪽 공백만 삭제

s = '########Hello, World!########'
print(s)
print(s.strip('#'))
print(s.lstrip('#'))
print(s.rstrip('#'))


# 문자열 찾기
s = 'www.silla.ac.kr'

# .kr찾기 => 제일 처음 문자의 즉 시작 번지수가 나온다.
print(s.find('.kr')) # 12번지가 나옴
print(s.find('x')) # 문자열에 문자가 없을 경우 -1이 출력된다.

# . 이 몇개인가?
print(s.count('.'))



