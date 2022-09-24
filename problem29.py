def linear_search(n,list):
    for i in range(0,len(list)):
        if list[i] == n:
            return True
            break
n = 10**2
lst = []
for a in range(2,n+1):
    for b in range(2,n +1):
        if linear_search(a**b,lst) == None:
            lst.append(a**b)

def insertion_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while(j>=0):
            if lst[j-1] > lst[j]:
                tmp = lst[j-1]
                lst[j-1] = lst[i]
                lst[i] = tmp
            j-=1
    return lst

#sample input: n=5
#sample output: 15
print(len(insertion_sort(lst)))

