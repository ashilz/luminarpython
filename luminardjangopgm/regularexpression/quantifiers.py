import re
#pattern="a+" # only check A
#pattern="a*" #any number of a including 0 number of 'a'
#pattern="a?"
#pattern="a{2}"##check two number of 'a'
pattern="a{2,3}"#check min two number of 'a' and max 3 number of 'a'
matcher=re.finditer(pattern,"aaaa bbbaaaabababbaaaaabbabaaaabaaaaaa3a$$aaababb bababbababa")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count += 1
print("count ",count)