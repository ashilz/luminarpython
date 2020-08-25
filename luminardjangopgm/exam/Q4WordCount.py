ques="hello hai hello hai"

word_count=ques.split(" ")
dict={}
for word in word_count:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
for k,v in dict.items():
    print(k,",",v)