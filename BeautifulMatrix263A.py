matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

element_to_find = 1
for i, row in enumerate(matrix):
    if element_to_find in row:
        col_index = row.index(element_to_find)
        print(abs(2-i)+abs(2-col_index))
        break
