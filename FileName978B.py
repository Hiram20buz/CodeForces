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
    kill(total)
    
print(n-len(total)) 
