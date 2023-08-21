user = list(input())
userD = set(user) 
'''
if len(userD)%2:
    print("IGNORE HIM!")
    
else:
    print("CHAT WITH HER!")
'''    
print("IGNORE HIM!" if len(userD)%2 else "CHAT WITH HER!")
