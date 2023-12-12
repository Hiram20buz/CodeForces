input_list = input().split()

result_list = list(map(int, input_list))

suma = 0
i = 1
while(i <= result_list[2]):
    suma = suma + result_list[0] * i
    i = i+1
    #print(suma)
  
if (suma < result_list[1]):
    print(0)
else:
    print(abs(suma - result_list[1]))
