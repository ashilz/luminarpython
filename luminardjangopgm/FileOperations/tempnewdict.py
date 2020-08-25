f=open("tempdate","r")
dict={}



for lines in f:
    district,temprature=lines.rstrip("\n").split(",")

    #data=
   #district=data[0]
    #temprature=data[1]
    if(district not in dict):
        dict[district]=temprature
    else:
        old=dict[district]
        if(temprature>old):
            old=dict[district]

print(dict)