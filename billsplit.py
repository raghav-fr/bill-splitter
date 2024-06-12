total=int(input("enter total value:"))
noPeople=int(input("enter the number of people"))
y=total/noPeople
people=[]
for i in range(noPeople):
    name=input("enter name:")
    value=int(input("enter value:"))
    if(value==0):
        valtogive=y
        valtoget=0
    if(value>0):
        if(value<y):
            valtogive=y-value
            valtoget=0
        else:
            valtogive=0
            valtoget=value-y
    
    person={"name":name,"value":value,"valtogive":valtogive,"valtoget":valtoget}

    people.append(person)

for i in people:
    for j in people:
        if(i['valtogive']>0):
            if(j['valtoget']>=i['valtogive']):
                
                print(i['name']," will give ",i['valtogive']," to ",j['name'])
                j['valtoget']-=i['valtogive']
                i['valtogive'] = 0


for i in people:
    for j in people:
        if(i['valtogive']>0):
            if(j['valtoget']<=i['valtogive'] and j['valtoget']>0.0):
                diff=j["valtoget"]
                print(i['name']," will give ",j['valtoget']," to ",j['name'])
                j['valtoget']-=diff
                i['valtogive'] -= diff 
