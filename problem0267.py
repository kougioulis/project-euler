def total(f,heads):
    return (1 + 2*f)**(heads)*(1 - f)**(1000 - heads)
    
f = 0.001 #start with 1 percent of cash
step = 0.0001 #increment 
optimal_f = 0
optimal_heads = 1000 #heads \in \left\{0,1,\cdots,1000 \right\} 

while f < 0.5:
    heads = 1
    while total(f,heads) < 10**9:
        heads +=1
    if heads < optimal_heads:
        optimal_f = f
        optimal_heads = heads
    f += step

print(optimal_f)
