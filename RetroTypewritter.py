t = input().replace("bS","\\").replace(" ","").replace("sQ","'").replace("nl","\n").replace("sp"," ")+" "
p=t[0]
m=""
i=0
while i!=(len(t)-1):
    if t[i].isdigit():
        if t[i+1].isdigit():
            j = int(t[i]+t[i+1])
            p+=j*t[i+2]
        elif t[i+1].isdigit():
            j = int(t[i])
            p+=j*t[i+1]        
        elif not t[i-1].isdigit():
            j = int(t[i])
            p+=j*t[i+1]       
    else:p+=t[i+1]
    i+=1
for i in p:
    if i.isdigit():pass
    else:m+=i
print(m[:-1])
