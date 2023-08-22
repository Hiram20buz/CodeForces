'''
x=[]
for _ in range(int(input())):
    if(input().lower() == 'yes'):
        x.append('YES')
        
    else:
        x.append('NO')
        
'''
lst = ['YES' if input().lower() == 'yes' else 'NO' for _ in range(int(input()))]

for _ in lst:
    print(_)
