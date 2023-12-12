def check_sum_of_other_two(nums):
    a, b, c = nums
    return a == b + c or b == a + c or c == a + b
    
ans = []
for i in range(int(input())):
    input_list = input().split()
    result_list = list(map(int, input_list))
    result = check_sum_of_other_two(result_list)
    
    if result:
        ans.append("YES")
    else:
        ans.append("NO")
        
for i in ans:
    print(i)
