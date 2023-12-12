input_list = input().split()

result_list = list(map(int, input_list))

suma = 0
for i in range(1,result_list[2]+1):
    suma = suma + result_list[0] * i
    
print(abs(suma - result_list[1]))
