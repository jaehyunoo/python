'''
    작성일 : 2023년 10월 18일
    작성자 : 컴소부 202095061 유재현
    설명 : P.195 심화문제 7.1
      다음과 같이 파이썬 프로그램을 실행할 적에, 다음 밑줄 안에 들어갈 알맞은 결과는 무엇인가? 미리 예측해본 후 실행시켜보고 그 결과를 적으시오.
'''

num_list = [100,200,300,400,500,600,700,800]
high = 6
low = 3

# 예측 : num_list안에서 6(high)번지인 700이 출력된다.
print(num_list[high])

# 예측 : num_list안에서 6(high)-2 = 4번지인 500이 출력된다.
print(num_list[high-2])

# 예측 : num_list안에서 6(high)-3(low) = 3번지인 400이 출력된다.
print(num_list[high - low])

# 예측 : num list안에서 숫자계산 3(low) - 6(high) = -3번지 즉 마지막에서 역순으로 세번 째 항목인 600이 출력된다.
print(num_list[low - high])

# 예측 : num list 안에서 -1번지 즉 마지막에서 첫 번째 항목인 800이 출력된다.
print(num_list[-1])

# 예측 : num list 안에서 -3(-low)번지 즉 마지막에서 세 번쨰 항목인 600이 출력된다.
print(num_list[-low])

# 예측 : num list 안에서 숫자의 계산 2*3 = 6번지인 700이 출력된다.
print(num_list[2 * 3])

# 예측 : num_list 안의 2번지인 300에 3을 곱한 900이 출력된다.
print(num_list[2] * 3)

# 예측 : num_list 안에서 5 % 4 = 1번지인 200이 출력된다.
print(num_list[5 % 4])

# 예측 : num_list의 길이 즉 안의 항목의 갯수가 출력이되는데 리스트항목이 총 8개이므로 8이 출력된다.
print(len(num_list))

# 예측 : num_list 안의 항목들중 최소값인 100이 출력된다.
print(min(num_list))

# 예측 : num_list 안의 항목들중 최대값인 800이 출력된다.
print(max(num_list))

# 예측 : num_list 안의 0번지부터 2번지까지 = [100,200,300] 출력된다.
print(num_list[:3])

# 예측 : num_list 안의 1번지부터 4번지까지 = [200,300,400,500] 출력된다.
print(num_list[1:5])

# 예측 : num_list 안의 마지막 번지(-1번지)부터 역순으로 마지막에서 네번째 번지(-4번지)까지 = [800,700,600,500] 출력한다.
print(num_list[-1:-5:-1]) # 시작 인덱스  : -1  /  끝 인덱스 : -5 / 스텝(간격) -1(역순) 

# 예측 : num_list 마지막에서 다섯 번째 번지(-5번지)부터 순서대로 마지막에서 두 번째 번지(-2)까지 = [400,500,600,700] 출력한다.
print(num_list[-5:-1:1])
