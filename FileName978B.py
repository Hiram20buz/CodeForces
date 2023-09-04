import re
n=int(input())
total=input()
lst=[]

def remove_char(lst, char):
    del lst[lst.index(char)]
    
if re.search('xxx', total):
    print('xxx in string')
else:
    print('Not xxx in string')
    print(0)
    
    
'''
import re
lst = ['x', 'x', 'x', 'i', 'i', 'i']
def remove_char(lst, char):
    del lst[lst.index(char)]
     
st="".join(lst)
print(st)
while (re.search('xxx', st)):
    remove_char(lst, 'x')
    print(lst)
    
'''
