input_list = input().split()

result_list = list(map(int, input_list))

def check_sum_of_other_two(nums):
    a, b, c = nums
    return a == b + c or b == a + c or c == a + b


result = check_sum_of_other_two(result_list)

if result:
    print("YES")
else:
    print("NO")
