line="hai hello hai hello"
#word count hai,2 and hello,2

words=line.split(" ")
print(words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)