n=int(input())
lst=[]
x=n//2
'''
if(n % 2 !=0):
    lst.append(3)
    lst.extend([2] * (x-1))
    
else:
    lst.extend([2] * (x))
   
''' 
lst.extend([3] + [2] * (x - 1)) if n % 2 != 0 else lst.extend([2] * x)

print(len(lst))
print(*lst)
