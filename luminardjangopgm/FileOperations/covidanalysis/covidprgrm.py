f=open("covid_19_india.csv", "r")
dict={}
dict1={}
total_confirmed=0
total_death=0
maxtotalcases=0
maxdeathcases=0
for lines in f:
    #print(lines)
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[8]
    death_cases=data[7]
    #print(state,",",case)
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases

    if(state not in dict):
        dict1[state]=death_cases
    else:
        dict1[state]=death_cases

print("***************************************")
print("STATE TOTAL CASES")

#print(dict)
for k,v in dict.items():
    print(k,":",v)
    total_confirmed+=int(v)
    if int(v)>maxtotalcases:
        maxtotlcases=int(v)
        maxtotalstate=k
    
    

print("***************************************")
print("STATE DEATH CASES")
for k,v in dict1.items():
    print(k,":",v)
    total_death+=int(v)
    if int(v)>maxtotalcases:
        maxdeathcases=int(v)
        maxdeathstate=k

print("***************************************")

print("Total death in India                  : ",total_death)
print("Total confirmed cases in India        : ",total_confirmed)
print("State with highest confrimed cases    : ",maxtotalcases,"(",maxtotalstate,")")
print("State with highest death cases        : ",maxdeathcases,"(",maxdeathstate,")",)
        