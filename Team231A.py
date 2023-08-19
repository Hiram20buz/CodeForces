x=0
for i in range(int(input())):
    total = sum(map(int,input().split()))
    if(total > 1):
        x += 1
    
print(x)
