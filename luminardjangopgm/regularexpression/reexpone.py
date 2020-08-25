#for pattern matching
#step 1 we have to import re module

import re

matcher=re.finditer("ab","ababababababcccbababcbabcbab")
count=0
for match in matcher:
    print(match.start())#postion of the char
    print(match.group())#group of the char
    count+=1
print(count)
