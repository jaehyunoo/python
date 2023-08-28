sum,i=0,0

for i in range(1,11):
    if i % 3 == 0:
        continue
    sum += 1

print("1부터 10까지의 숫자 중 3의배수를 제외한 모든 숫자의합:",sum)