x = (n:=int(input())) // 2
if(n % 2 !=0):
    '''
    print(x:=n//2)
    print(' '.join(['3'] + ['2'] * (x-1)))
    '''
    print(f"{x}\n{' '.join(['3'] + ['2'] * (x - 1))}")
else:
    '''
    print(x:=n//2)
    print(' '.join(['2'] * x))
    '''
    print(f"{x}\n{' '.join(['2'] * x)}")
