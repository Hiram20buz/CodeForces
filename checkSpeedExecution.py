import time

start_time = time.time()

# Your code here
#w=int(input('Weight: '))
print("NO" if 1 % 2 else "YES")

end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
