lst=[]

for i in range(int(input())):
    #w = input()
    #w := input())
    #size = len(w)
    #size = len(w := input())
    #size := len(w := input())
    lst.append((w[0]+str(size-2)+w[size-1]) if (size := len(w := input())) > 10 else w)

for i in lst:
    print(i)
