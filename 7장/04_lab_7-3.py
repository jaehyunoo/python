'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : 도시의 인구 자료에 대한 슬라이싱을 해보자
'''
# 리스트 저장
p_list = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

# 요구하는 내용 출력
print("서울인구", p_list[1])    # 리스트 항목중 1번지에 해당하는 항목 출력
print("인천인구", p_list[-1])   # -1을 넣으면 리스트 중 제일 마지막 항목출력
print("도시리스트",p_list[0::2]) # 도시리스트를 0번지부터 2씩 증가하는 번지에 항목들만 출력
'''
 도시리스트를 출력하는 다른방법 (변수에 저장)
    city_list = p_list[0::2]
    print("도시 리스트", city_list)
'''
people = p_list[1::2] # people 변수에 리스트에 1번지부터 2씩 증가하는 번지에 항목들을 변수에 저장
print("인구의 합:", sum(people)) # people 변수에 들어간 항목들의 합을 구하는 것

