list = [1]
dim=5
i=0
increment=2

while len(list) < 2*dim -1:
    tmp=i;
    while (i < (tmp+ 4)):
        list.append(list[i]+increment)
        i= i+1
    increment = increment+2
        
print(sum(list))
