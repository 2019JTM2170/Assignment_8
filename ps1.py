count1=0 #initializing counters
count2=0
start=0
ps=""

#########PARITY#########################

st=input() #Take input bit stream as a string
l=[char for char in st] #converting string to a list
for c in l:
    if c=='1':
        count1+=1;
if count1%2==0:  #checking for parity
    l.append('1')
else:
    l.append('0')
print("Parity bit data:",end='')
ps=ps.join(l) #priniting parity bit stream
print(ps)


########FRAMING####################

i=0
new=""
l1=[char for char in ps]
while(i<len(l1)):
    if l1[i]=='0' and l1[i+1]=='1' and l1[i+2]=='0':
        l1.insert(i+3,'0')
        i=i+4
    else:
        i=i+1
        
l1.append('0')
l1.append('1')
l1.append('0')
l1.append('1')

print("Transmitting data:",end='')
new=new.join(l1)
print(new)







