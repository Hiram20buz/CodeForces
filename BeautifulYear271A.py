l=list(input())
num=int(''.join(map(str, l)))
for i in range(num+1,9100):
    if(len(set(str(i))) == len(str(i))):
        print(i)
        break
