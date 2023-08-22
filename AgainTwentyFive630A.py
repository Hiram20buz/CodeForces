expo=int(input())
lst=[]
sum=1
while True:
    if expo == 1:
        break
    expo=expo//2
    sum=sum*(5**expo)
    
print(5*sum)
    
    
    
