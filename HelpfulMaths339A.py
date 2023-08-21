total=list(map(int,input().split('+')))
total.sort()

nums = map(str, total)
result = '+'.join(nums)

print(result)  
