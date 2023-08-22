#Dynamic programming
#limit conditions: coin_count(coins,n,0) = 1
#                 coin_count(coins,0,n) < 0
def coin_count(coins, n, total):
    if (total == 0):
        return 1
    if total < 0 or n <= 0:
        return 0
  
    return coin_count(coins, n - 1, total) + coin_count(coins, n, total-coins[n-1])
  
  
coins = [1,2,5,10,20,50,100,200]
n = len(coins)
total = 5
print(coin_count(coins,n,total))
