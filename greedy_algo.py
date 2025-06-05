#using greedy algo for the coin change problem
def greedy(arr, amt, c):
    arr.sort(reverse=True)  #sorting the list in descending order
    coin_used = []
    for i in arr:
        while amt >= i:
                amt = amt - i
                coin_used.append(i)
                c += 1
    return coin_used, c  #we are returning both values as a tuple (ps: it's only working like this) 

arr = [10, 4, 30, 1]
coin_used, c = greedy(arr, 77, 0)
print("Coins used: ", coin_used)
print("Total coins: ", c)