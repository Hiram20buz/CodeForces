'''
A. Increasing and Decreasing
Ascending with decreasing difference: [1, 6, 10, 13, 15]
'''
t = int(input().strip())
for _ in range(t):
    x, y, n = map(int, input().strip().split())
    cnt = 1
    v = [0] * n
    v[-1] = y
    v[0] = x
    for i in range(n - 2, 0, -1):
        v[i] = v[i + 1] - cnt
        cnt += 1
    if v[1] - v[0] > v[2] - v[1]:
        print(' '.join(map(str, v)))
    else:
        print(-1)
