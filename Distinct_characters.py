#n=input('')
l=input("")
l=l.lower()
#a=n.split()
temp=[]
v=''
for element in l: #elmt there in a
    if(element not in temp):
        if element==' ':
            continue
        else:
            temp.append(element) 
r=sorted(temp)
for i in r:
    if i==' ':
        continue
    else:
        v+=i
print(v)
        
