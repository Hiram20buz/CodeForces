(lst:=[]).append(input().lower())
lst.append(input().lower())
 
if(lst[0] < lst[1]):
    print(-1)
    
elif(lst[0] > lst[1]):
    print(1)
    
else:
    print(0)
