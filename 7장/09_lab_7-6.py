'''
    작성일 : 2023년 11월 1일
    작성자 : 컴소부 202095061 유재현
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765), ('부산',3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

max_population = city_info[0][1] # 첫 번째 항목이 기준
min_population = city_info[0][1]
total_population = 0

max_city = city_info[0][0] # 첫 번째 항목이 기준
min_city = city_info[0][0]

# 도시명 , 인구수를 각각 변수에다가 담았다.
for city, population in city_info:
    total_population += population
    if population > max_population :
        max_population = population
        max_city = city
    if population < min_population :
        min_population = population
        min_city = city

print('최대인구 : {}, 인구 : {} 천명'.format(max_city, max_population))
print('최소인구 : {}, 인구 : {} 천명'.format(min_city, min_population))
print('리스트 도시 평균 인구 : {}천명'.format(total_population / len(city_info)))