'''
    작성일 : 2023년 11월 1일
    작성자 : 컴소부 202095061 유재현
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''

# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765), ('부산',3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

# 최대값을 구하기위한 값 초기화 -> 비교하기 위해 실제 최대 인구보다 작은값으로 설정해둔다.
max_population = 0
# 최소값을 구하기위한 값 초기화 -> 비교하기 위해 실제 최소 인구보다 큰값으로 설정해둔다.
min_population = 999999999999999999
# 모든 도시의 인구의 평균을 구하기 위한 값 초기화
total_population = 0
# max_city와 min_city는 각각 최대와 최소 인구를 가진 도시의 정보를 저장하기 위한 변수로 초기화.
max_city = None
min_city = None

# 반복문을 사용하여 city_info 리스트의 각 도시를 돌려보며 최대, 최소 인구를 찾고 모든 도시의 인구를 합산한다.
for city in city_info:
    # 리스트안 각 튜플의 1번지 즉 인구수를 다 더한다
    total_population += city[1]
    # 리스트안 튜플의 1번지 즉  인구수가 가장 많은 도시의 인구수와 도시의 이름을 구한다.
    if city[1] > max_population :
        max_population = city[1]
        max_city = city
    # 리스트안 튜플의 1번지 즉 인구수가 가장 적은 도시의 인구수와 도시의 이름을 구한다
    if city[1] < min_population :
        min_population = city[1]
        min_city = city

print('최대인구 : {0}, 인구 : {1} 천명'.format(max_city[0], max_city[1]))
print('최소인구 : {0}, 인구 : {1} 천명'.format(min_city[0], min_city[1]))
# 도시평균의 인구는 리스트 안 각 튜플의 1 번지 즉 인구수를 다더한값에 city_info리스트안에들어가있는 튜플의 개수를 나누어주면 평균 인구수가된다.
print('리스트 도시 평균 인구 : {0}천명'.format(total_population / len(city_info)))