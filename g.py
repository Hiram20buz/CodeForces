import time

start_time = time.time()

# Your code here
for i in [((w[0]+str(size-2)+w[size-1]) if (size := len(w := "pneumonoultramicroscopicsilicovolcanoconiosis")) > 10 else w) for i in range(1) ]:
    print(i)

end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
