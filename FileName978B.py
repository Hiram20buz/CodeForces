import re
n=int(input())
total=list(input())
lst=[]

def remove_char(lst, char):
    del lst[lst.index(char)]
    
def kill(lst):     
    while (re.search('xxx', "".join(lst))):
        remove_char(lst, 'x')
    
if re.search('xxx', "".join(total)):
    #print('xxx in string')
    kill(total)
else:
    #print('Not xxx in string')
    print(0)
    
print(total)  
'''
import re
lst = ['x', 'x', 'x', 'i', 'i', 'i']
def remove_char(lst, char):
    del lst[lst.index(char)]
     
while (re.search('xxx', "".join(lst))):
    remove_char(lst, 'x')
    print(lst)
'''
