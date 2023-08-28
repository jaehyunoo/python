num = int(input('정수를입력하시오'))

print ('1000 단위',num % 10000 // 1000)
print ('100단위',num % 1000 // 100)
print ('10단위',num % 100 // 10)
print ('1단위', num % 10)