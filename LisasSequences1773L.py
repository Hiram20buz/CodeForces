n=list(map(int,input().split()))
k=list(map(int,input().split()))
def z(n,k):
    pass
    
def replace_with_zeros(lst, m):
    n = len(lst)
    for i in range(0,n, m):
        lst[i]=0

    return lst



new_list = replace_with_zeros(k, n[1])
print(new_list)
    
'''
    for i in range(n[0]-1):
        if(k[i] >= k[i+1]):
            x += 1
'''  


'''
k = [1, 2, 3, 4, 5,6,7,8,9,10]

for i in range(len(k) - 2):
    group = k[i:i+3]
    print(group)

'''
    
 
