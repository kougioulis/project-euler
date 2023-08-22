# Complexity O(n*value)

def coin_change(coins, value):
  
    ways = [1] + [0]*value
  
    for i in range(0, len(coins)):
        for j in range(i, value+1):
            ways[j] = ways[j] + ways[j-i]
  
    return ways[value]
  
  
coins = [1,2,5,10,20,50,100,200]
n = len(coins)

print(coin_change(coins,3)) 
